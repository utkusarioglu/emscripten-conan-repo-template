#!/bin/sh

. ./.config
. scripts/clean.sh

install() {
  conan install . 
  # \
  #   --output-folder $WEB_BUILD_DIR 
    # \
    # -s build_type=Release
}

build() {
  conan build . 
  # -b $WEB_BUILD_DIR
}

install
build
