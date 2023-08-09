#!/bin/bash

source ./repo.config
source scripts/common.sh

clean $@
install 'linux' $@
build 'linux' $@
