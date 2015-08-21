#!/bin/bash
set -x
./clean.sh
mv /vagrant/assignments/network-virtualization/topologySlice.py ~/pox/pox/misc/
pox.py log.level --DEBUG misc.topologySlice &
