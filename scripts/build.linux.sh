#!/bin/sh
.
. ./repo.config
. scripts/clean.sh

install() {
  target_profile=$1
  
  if [ -z "$target_profile" ]; then
    echo "Error: Target profile needs to be the first param"
    exit 1
  fi

  conan install . \
    -pr:b $(pwd)/profiles/host.profile \
    -pr:h $(pwd)/profiles/$target_profile.profile \
    --lockfile-out conan.lock \
    --lockfile conan.lock 
}

build() {
  target_profile=$1
  
  if [ -z "$target_profile" ]; then
    echo "Error: Target profile needs to be the first param"
    exit 1
  fi

  conan build . \
    -pr:b $(pwd)/profiles/host.profile \
    -pr:h $(pwd)/profiles/$target_profile.profile \
    --lockfile-out conan.lock \
    --lockfile conan.lock 
}

install 'linux'
build 'linux'
