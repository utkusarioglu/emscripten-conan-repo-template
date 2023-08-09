#!/bin/sh

. ./repo.config
. scripts/utils.sh

clean
install 'windows'
build 'windows'
