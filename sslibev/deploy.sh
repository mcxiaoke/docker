#!/bin/bash
# run on local machine
SERVER=$1 # root@vs.mcxiaoke.com
if [ -z "$1" ] 
then
    echo "No server supplied, format user@host, exit."
    exit 1
fi

ssh $SERVER 'rm -rf /opt/docker/sslibev && mkdir -p /opt/docker/sslibev' \
&& scp gen.py start.sh stop.sh mgr.sh $SERVER:/opt/docker/sslibev \
&& ssh $SERVER 'cd /opt/docker/sslibev && ./start.sh'

