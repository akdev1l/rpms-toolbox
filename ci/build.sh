#!/bin/bash

version="$1"
curl -L "https://github.com/akdev1l/toolbox/archive/refs/tags/${version}.tar.gz" \
  -o "$HOME/rpmbuild/SOURCES/${version}.tar.gz"

sudo dnf builddep -y --spec toolbox.spec
rpmbuild -ba toolbox.spec
