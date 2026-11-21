"""Check that bold UI labels in the user docs exist in the documented SITMUN version.

The admin manual and guides quote UI labels in bold (**Guarda**, **Registrar**).
Each bold phrase must be a label of the admin (es.json) or a seeded Spanish
translation (04-translations.sql) of the SITMUN version in zensical.toml
(extra.sitmun_version), or be listed exactly, with the same case, in
.github/label-allowlist.txt (bold used for emphasis, headings or names that are
not UI labels). A phrase matches a label ignoring case, exactly or as its
beginning before a bracket ("Campo de latitud" matches "Campo de latitud
(opcional)"). Paths like **Sistema** → **Idiomas** are checked part by part.
Both **bold** and __bold__ are read, also when wrapped over lines; code blocks
and inline code are skipped.

Usage: python .github/scripts/check_ui_labels.py [docs_dir]
Set SITMUN_SOURCE to a local sitmun checkout to read the files with git instead
of downloading them.
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import tomllib
import urllib.request

docs = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "docs")
version = tomllib.loads(pathlib.Path("zensical.toml").read_text())["project"]["extra"]["sitmun_version"]
FILES = ("sitmun-admin/src/assets/i18n/es.json",
         "sitmun-backend/src/main/resources/db/changelog/baseline/04-translations.sql")


def read(path: str) -> str:
    source = os.environ.get("SITMUN_SOURCE")
    if source:
        return subprocess.run(["git", "-C", source, "show", f"v{version}:{path}"],
                              check=True, capture_output=True, text=True).stdout
    url = f"https://raw.githubusercontent.com/sitmun/sitmun/v{version}/{path}"
    with urllib.request.urlopen(url, timeout=60) as response:
        return response.read().decode("utf-8")


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\\", "")).strip().rstrip(":*.").strip().lower()


labels = set()


def collect(node) -> None:
    if isinstance(node, dict):
        for value in node.values():
            collect(value)
    elif isinstance(node, str):
        labels.add(norm(node))


collect(json.loads(read(FILES[0])))
for match in re.finditer(r"lang\.lan_id, '((?:[^']|'')*)' FROM [^;]*?lan_shortname = 'es'", read(FILES[1])):
    labels.add(norm(match.group(1).replace("''", "'")))
prefixes = {label.split(" (")[0] for label in labels}

allowlist_file = pathlib.Path(".github/label-allowlist.txt")
allowed = {re.sub(r"\s+", " ", line).strip() for line in allowlist_file.read_text(encoding="utf-8").splitlines()
           if line.strip() and not line.startswith("#")}

FENCE = re.compile(r"^( *)(```|~~~).*?^\1\2[^\n]*$", re.M | re.S)
INLINE_CODE = re.compile(r"`[^`\n]+`")
# **bold** and ***bold italic***, also glued to letters (**Capa**s), and
# __bold__, but not __ inside words (SITMUN__DB__URL), as Python-Markdown reads them.
BOLD = re.compile(r"(?<!\*)(\*\*\*|\*\*)(?=\S)((?:(?!\n\s*\n).)+?)(?<=\S)\1(?!\*)"
                  r"|(?<![\w*])(__)(?=\S)((?:(?!\n\s*\n).)+?)(?<=\S)__(?![\w*])", re.S)

unknown = {}
for page in sorted(docs.rglob("*.md")):
    text = INLINE_CODE.sub("", FENCE.sub("", page.read_text(encoding="utf-8")))
    for match in BOLD.finditer(text):
        phrase = re.sub(r"\s+", " ", match.group(2) or match.group(4)).strip()
        if phrase in allowed:
            continue
        parts = [norm(part) for part in re.split(r"\s*→\s*", phrase)]
        if all(part in labels or part in prefixes for part in parts):
            continue
        unknown.setdefault(phrase, page)

for phrase, page in unknown.items():
    print(f"::error file={page}::**{phrase}** is not a label of SITMUN {version}; "
          "fix it, or add it to .github/label-allowlist.txt if it is not a UI label")
print(f"{len(labels)} labels of SITMUN {version}; {len(unknown)} unknown bold phrases")
sys.exit(1 if unknown else 0)
