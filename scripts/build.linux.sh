#!/bin/sh
.
. ./repo.config
. scripts/clean.sh

install() {
  conan install . \
    -pr:h $(pwd)/profiles/host.profile \
    -pr:b $(pwd)/profiles/build.profile \
    --lockfile-out conan.lock \
    --lockfile conan.lock 
}

build() {
  conan build . \
    -pr:h $(pwd)/profiles/host.profile \
    -pr:b $(pwd)/profiles/build.profile \
    --lockfile-out conan.lock \
    --lockfile conan.lock 
}

install
build
