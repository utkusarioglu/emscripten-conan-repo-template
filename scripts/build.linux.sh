#!/bin/bash

source .repo.config
source scripts/utils.sh

build 'linux' $@
run_test 'linux' $@
