#!/bin/sh

. ./.config
. scripts/clean.sh

install() {
  conan install . \
    -if $WEB_BUILD_DIR \
    -b missing \
    -pr:h profiles/wasm.profile \
    -pr:b profiles/build.profile
}

build() {
  conan build . -bf $WEB_BUILD_DIR
}

install
build
