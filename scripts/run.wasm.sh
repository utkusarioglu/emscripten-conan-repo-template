#!/bin/bash

cd public

echo 'Starting python server at port 80…'
python3 -m http.server 80
