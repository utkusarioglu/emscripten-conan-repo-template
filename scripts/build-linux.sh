#!/bin/sh
.
. ./repo.config
. scripts/clean.sh

install() {
  conan install . \
    --output-folder $LINUX_BUILD_DIR \
    -pr:h $(pwd)/profiles/host.profile \
    -pr:b $(pwd)/profiles/build.profile
    # \
    # -s build_type=Release
}

build() {
  cp CMakeLists.txt $LINUX_BUILD_DIR/CMakeLists.txt
  conan build . \
    --output-folder $LINUX_BUILD_DIR \
    -pr:h $(pwd)/profiles/host.profile \
    -pr:b $(pwd)/profiles/build.profile
    # \
    # --output-folder $WEB_BUILD_DIR 
}

install
build
