#!/bin/sh

. ./.config
. scripts/clean.sh

install() {
  conan install . \
    -if $WEB_BUILD_DIR \
    -b missing
}

build() {
  conan build . -bf $WEB_BUILD_DIR
}

install
build
