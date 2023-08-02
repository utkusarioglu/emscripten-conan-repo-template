#!/bin/sh
.
. ./repo.config
. scripts/clean.sh

install() {
  conan install . \
    --output-folder $LINUX_BUILD_DIR 
    # \
    # -s build_type=Release
}

build() {
  conan build . \
    --output-folder $LINUX_BUILD_DIR 
    # -b $WEB_BUILD_DIR 
    # \
    # --output-folder $WEB_BUILD_DIR 
}

install
cp CMakeLists.txt $LINUX_BUILD_DIR/CMakeLists.txt
build
