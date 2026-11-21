#!/usr/bin/env bash
# Check that a dev container variant started what its page promises.
# Usage: check-sitmun.sh demo|vacia|osm   (after start-sitmun.sh, same SITMUN_* settings)
set -euo pipefail
VARIANT="$1"
PORT="${SITMUN_PORT:-9000}"
PROJECT="${SITMUN_PROJECT:-sitmun}"
DIR="${SITMUN_DIR:-$HOME/sitmun}"
BASE="http://localhost:$PORT"
fail=0
check() { if [ "$2" = "$3" ]; then echo "ok   $1: $2"; else echo "FAIL $1: $2 (expected $3)"; fail=1; fi; }
code() { curl -s -o /dev/null -w '%{http_code}' "$1"; }
sql() { (cd "$DIR" && docker compose -p "$PROJECT" exec -T postgres sh -c "psql -At -U \"\$POSTGRES_USER\" -d \"\$POSTGRES_DB\" -c \"$1\""); }

check "administrador" "$(code "$BASE/admin/")" 200
check "visor" "$(code "$BASE/viewer/")" 200
check "primera visita (asistente)" "$(curl -s "$BASE/backend/api/setup/status" | python3 -c 'import sys,json;print(json.load(sys.stdin)["firstRun"])')" True
apps=$(curl -s "$BASE/backend/api/config/client/application" | python3 -c 'import sys,json;print(len(json.load(sys.stdin).get("content",[])))')
all_apps=$(sql "select count(*) from stm_app" | tr -d '\r')
osm=$(sql "select count(*) from stm_app_bckg a join stm_backgrd b on b.bac_id=a.abc_backid where b.bac_name='OpenStreetMap'" | tr -d '\r')
atleast() { [ "$1" -ge "$2" ] && echo ">=$2" || echo "$1"; }
case "$VARIANT" in
  demo)  check "aplicaciones públicas" "$(atleast "$apps" 1)" ">=1"
         check "mapa de fondo OpenStreetMap de la demostración" "$(atleast "$osm" 1)" ">=1" ;;
  vacia) check "aplicaciones" "$all_apps" 0 ;;
  osm)   check "aplicaciones públicas" "$(atleast "$apps" 1)" ">=1"
         check "mapa de fondo OpenStreetMap de la demostración, quitado" "$osm" 0 ;;
  *) echo "variante desconocida: $VARIANT"; exit 2 ;;
esac
exit $fail
