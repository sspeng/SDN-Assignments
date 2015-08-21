#!/bin/bash
rsync -vrtC * zi:~/Coursera-SDN/${PWD##*/}
#scp -r -P 8870 ../graph500-distributed/ youwei@166.111.68.162:~
