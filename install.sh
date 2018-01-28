#!/bin/sh
brew install libav
brew link --overwrite python3

pip3 install -r server_require.txt