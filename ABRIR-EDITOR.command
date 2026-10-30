#!/bin/zsh
cd -- "${0:A:h}"
if curl -fsS http://127.0.0.1:5190/ >/dev/null 2>&1; then
 open http://127.0.0.1:5190/
 exit 0
fi
if ! command -v node >/dev/null; then
 export PATH="$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin:$PATH"
fi
(sleep 2; open http://127.0.0.1:5190/) &
exec node server/local.mjs
