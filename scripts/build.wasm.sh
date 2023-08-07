#!/bin/sh

. ./repo.config
. scripts/clean.sh

install() {
  target_profile=$1
  
  if [ -z "$target_profile" ]; then
    echo "Error: Target profile needs to be the first param"
    exit 1
  fi

  conan install . \
    -b 'missing' \
    -pr:h profiles/wasm.profile \
    -pr:b profiles/host.profile \
    --lockfile-out conan.lock \
    --lockfile conan.lock 
}

build() {
  conan build . \
    -pr:h profiles/wasm.profile \
    -pr:b profiles/host.profile \
    --lockfile-out conan.lock \
    --lockfile conan.lock 
}

install 'wasm'
build 'wasm'
