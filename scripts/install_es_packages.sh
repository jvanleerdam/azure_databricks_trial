#!/bin/bash
set -e

PIP_PATH="/databricks/python/bin/pip"
ES_PACKS_PATH="/eskapade_packages"
ES_PACKS_ARCHIVE="/dbfs/user/eskapade/eskapade.tar.gz"

# create directory for Eskapade packages
mkdir "$ES_PACKS_PATH"

# install Eskapade
cd "$ES_PACKS_PATH"
mkdir eskapade
echo "Installing Eskapade in $( pwd )/eskapade"
tar -C eskapade --no-same-owner -xzf "$ES_PACKS_ARCHIVE"
"${PIP_PATH}" install -e eskapade
