#!/bin/sh

. ./repo.config
. scripts/common.sh

clean
install 'windows'
build 'windows'
