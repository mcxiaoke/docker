#!/bin/bash

#docker pull shadowsocks/shadowsocks-libev

start(){
    echo "====== Adding shadowsocks-libev servers......"
    #ufw allow $i
    for ((i=BEGIN;i<=END;i++)); do
        echo "====== Start docker container sslibev_$i"
        docker run -d  --restart=always --name sslibev_$i \
        -e PASSWORD=$PASSWORD \
        -e SERVER_PORT=$i -e METHOD=$METHOD \
        -p $i:$i -p $i:$i/udp shadowsocks/shadowsocks-libev
    done
    echo "====== Running sslibev servers:"
    docker ps | grep sslibev
}

stop(){
    echo "====== Running sslibev servers:"
    docker ps | grep sslibev
    echo "====== Removing shadowsocks-libev servers......"
    for ((i=BEGIN;i<=END;i++)); do
        echo "====== Stop docker container sslibev_$i"
        docker stop sslibev_$i
        docker container rm sslibev_$i
    done
}

restart(){
    echo "====== Restarting shadowsocks-libev servers......"
    for ((i=BEGIN;i<=END;i++)); do
        echo "====== Restart docker container sslibev_$i"
        docker restart sslibev$i
    done
}

PASSWORD=shadowsocks
METHOD=aes-256-cfb
SERVER_PORT=9011

if [[ "$2" =~ ^[0-9]{4,}$ ]]; then
    SERVER_PORT=$2
fi

BEGIN=SERVER_PORT
END=$((SERVER_PORT + 4))

if [[ $1 == "start" ]]; then
    start
elif [[ $1 == "stop" ]]; then
    stop
elif [[ $1 == "restart" ]]; then
    restart
else
    echo "Usage: $0 [start|stop|restart] [server_port (only for start >1024)]."
fi

