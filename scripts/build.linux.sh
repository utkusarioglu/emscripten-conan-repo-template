#!/bin/sh
.
. ./repo.config
. scripts/common.sh

clean
install 'linux'
build 'linux'
