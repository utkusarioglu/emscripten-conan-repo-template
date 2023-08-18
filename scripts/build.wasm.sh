#!/bin/bash

source ./repo.config
source scripts/utils.sh

clean 'wasm' $@
install 'wasm' $@
build 'wasm' $@
