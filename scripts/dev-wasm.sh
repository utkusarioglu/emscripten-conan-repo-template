#!/bin/sh

. scripts/build-wasm.sh

if [ -e /var/run/nginx.pid ]; then 
  echo "Reloading nginx..."
  nginx -s reload -c $(pwd)/nginx.conf
fi
