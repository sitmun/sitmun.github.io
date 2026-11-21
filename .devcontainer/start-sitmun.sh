#!/usr/bin/env bash
# Start SITMUN from the published images (no build) for a dev container variant.
#
# Settings (environment variables):
#   SITMUN_PROFILE   profile in profiles/ of sitmun/sitmun: showcase (demo data) or postgres (empty)
#   SITMUN_EXTRA     extra compose profiles, for example "demo" for the example database
#   SITMUN_SCENARIO  optional SQL file applied to the SITMUN database once it is up
#   SITMUN_VERSION   default 1.3.0
#   SITMUN_PORT      published front port, default 9000
#   SITMUN_PROJECT   compose project name, default sitmun
#   SITMUN_DIR       where sitmun/sitmun is cloned, default ~/sitmun
#
# In a codespace the public address is the forwarded HTTPS address of the front
# port; elsewhere it is http://localhost:<port>. SITMUN builds the admin, API and
# proxy links from PUBLIC_*, so they must match the address the browser uses.
set -euo pipefail

PROFILE="${SITMUN_PROFILE:?set SITMUN_PROFILE}"
EXTRA="${SITMUN_EXTRA:-}"
SCENARIO="${SITMUN_SCENARIO:-}"
VERSION="${SITMUN_VERSION:-1.3.0}"
PORT="${SITMUN_PORT:-9000}"
PROJECT="${SITMUN_PROJECT:-sitmun}"
DIR="${SITMUN_DIR:-$HOME/sitmun}"
if [ -n "$SCENARIO" ]; then
  SCENARIO="$(cd "$(dirname "$SCENARIO")" && pwd)/$(basename "$SCENARIO")"
fi

if [ ! -d "$DIR/.git" ]; then
  git -c advice.detachedHead=false clone --quiet --depth 1 --branch "v$VERSION" https://github.com/sitmun/sitmun.git "$DIR"
fi
cd "$DIR"

if [ ! -f .env ]; then
  cp "profiles/$PROFILE.env" .env
  # The three secrets that setup.sh would generate.
  for key in SITMUN_USER_SECRET MIDDLEWARE_SECRET SITMUN_MBTILES_JOB_HANDLE_SECRET; do
    echo "$key=$(openssl rand -hex 32)" >> .env
  done
fi

if [ -n "${CODESPACE_NAME:-}" ]; then
  SCHEME=https
  HOST="${CODESPACE_NAME}-${PORT}.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
  PUBLIC_PORT=443
else
  SCHEME=http
  HOST=localhost
  PUBLIC_PORT="$PORT"
fi
PROFILES="postgres${EXTRA:+,$EXTRA}"
# Replace any earlier values so a restarted codespace keeps working.
sed -i.bak -E '/^(COMPOSE_PROFILES|PUBLIC_URL_SCHEME|PUBLIC_HOSTNAME|PUBLIC_PORT|LOCAL_PORT)=/d' .env && rm -f .env.bak
cat >> .env <<VARS
COMPOSE_PROFILES=$PROFILES
PUBLIC_URL_SCHEME=$SCHEME
PUBLIC_HOSTNAME=$HOST
PUBLIC_PORT=$PUBLIC_PORT
LOCAL_PORT=$PORT
VARS

docker compose -p "$PROJECT" up -d --pull always --no-build

echo "Esperando a SITMUN en el puerto $PORT..."
ready=false
for _ in $(seq 1 120); do
  if curl -fs -o /dev/null "http://localhost:$PORT/backend/api/setup/status"; then
    ready=true
    break
  fi
  sleep 5
done
if [ "$ready" != true ]; then
  echo "SITMUN no ha respondido en 10 minutos. Revisa: docker compose -p $PROJECT logs backend" >&2
  exit 1
fi

# The scenario runs once: later starts keep what the user has done since.
if [ -n "$SCENARIO" ] && [ ! -f .scenario-applied ]; then
  docker compose -p "$PROJECT" exec -T postgres \
    sh -c 'psql -q -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DB"' < "$SCENARIO"
  touch .scenario-applied
fi

BASE="$SCHEME://$HOST"
[ "$SCHEME" = http ] && BASE="$BASE:$PORT"
echo
echo "SITMUN $VERSION está en marcha:"
echo "  Administrador: $BASE/admin/   (la primera visita pide la contraseña de admin)"
echo "  Visor:         $BASE/viewer/"
