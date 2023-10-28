#!/bin/sh

. .repo.config
. scripts/utils.sh

build 'windows' $@
install 'windows'
