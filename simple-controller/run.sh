#!/bin/bash
set -x
mv /vagrant/assignments/simple-controller/firewall.py ~/pox/pox/misc/
pox.py  forwarding.l2_learning misc.firewall
