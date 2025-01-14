#!/bin/bash
set -ef -o pipefail

WEBPACK_HOST='0.0.0.0'
WEBPACK_PORT='8042'

if [[ "$1" == "--install" ]] ; then
yarn install --immutable && echo "Finished yarn install"
fi
# Start the webpack dev server on the appropriate host and port
node ./hot-reload-dev-server.js --host "$WEBPACK_HOST" --port "$WEBPACK_PORT"
