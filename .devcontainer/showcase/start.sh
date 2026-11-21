#!/usr/bin/env bash
# Start the SITMUN showcase from the published images (no build).
# In a codespace, the public address is the forwarded HTTPS address of port 9000;
# elsewhere it is http://localhost:<port>. SITMUN builds the admin, API and proxy
# links from PUBLIC_*, so they must match the address the browser uses.
set -euo pipefail

VERSION="${SITMUN_VERSION:-1.3.0}"
PORT="${SHOWCASE_PORT:-9000}"
PROJECT="${SHOWCASE_PROJECT:-sitmun-showcase}"
DIR="${SHOWCASE_DIR:-$HOME/sitmun-showcase}"

if [ ! -d "$DIR/.git" ]; then
  git -c advice.detachedHead=false clone --quiet --depth 1 --branch "v$VERSION" https://github.com/sitmun/sitmun.git "$DIR"
fi
cd "$DIR"

if [ ! -f .env ]; then
  cp profiles/showcase.env .env
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
# Replace any earlier values so a restarted codespace keeps working.
sed -i.bak -E '/^(COMPOSE_PROFILES|PUBLIC_URL_SCHEME|PUBLIC_HOSTNAME|PUBLIC_PORT|LOCAL_PORT)=/d' .env && rm -f .env.bak
cat >> .env <<VARS
COMPOSE_PROFILES=postgres,demo
PUBLIC_URL_SCHEME=$SCHEME
PUBLIC_HOSTNAME=$HOST
PUBLIC_PORT=$PUBLIC_PORT
LOCAL_PORT=$PORT
VARS

docker compose -p "$PROJECT" up -d --pull always --no-build

echo "Esperando a SITMUN en el puerto $PORT..."
for _ in $(seq 1 90); do
  if curl -fs -o /dev/null "http://localhost:$PORT/backend/api/setup/status"; then
    break
  fi
  sleep 5
done

BASE="$SCHEME://$HOST"
[ "$SCHEME" = http ] && BASE="$BASE:$PORT"
echo
echo "SITMUN $VERSION (showcase) está en marcha:"
echo "  Administrador: $BASE/admin/   (la primera visita pide la contraseña de admin)"
echo "  Visor:         $BASE/viewer/"
