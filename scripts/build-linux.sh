#!/bin/sh
.
. ./repo.config
. scripts/clean.sh

install() {
  conan install . \
    -pr:h $(pwd)/profiles/host.profile \
    -pr:b $(pwd)/profiles/build.profile 
}

build() {
  # cp CMakeLists.txt $LINUX_BUILD_DIR/CMakeLists.txt
  conan build . \
    -pr:h $(pwd)/profiles/host.profile \
    -pr:b $(pwd)/profiles/build.profile 
}

install
build
