#!/bin/sh

. ./repo.config
. scripts/common.sh

clean
install 'wasm'
build 'wasm'
