#!/bin/bash

source ./repo.config
source scripts/utils.sh

clean $@
install 'linux' $@
build 'linux' $@
