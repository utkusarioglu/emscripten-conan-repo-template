#!/bin/sh

echo "Building..."
. scripts/build-linux.sh

echo "\n\n\nRunning..."
. scripts/run-linux.sh $1
