#!/bin/bash

source .repo.config
source scripts/utils.sh

build 'wasm' $@
