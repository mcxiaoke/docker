# Intro

Shadowsocks-libev server dockerfile, customize with gen.py and docker-compose.

# Usage

## use docker run
```sh
docker pull dockercat/sslibev
docker run --restart=always -d -e PASSWORD=<password> -p8388:8388 -p8388:8388/udp --name sslibev dockercat/sslibev
docker ps | grep sslibev # status
```

## use docker-compose (recommended)
```sh
docker pull dockercat/sslibev
# generate docker-compose.yml
# apt install docker-compose
# apt install python-pip3 -y
# pip3 install click
python3 gen.py # config
docker-compose up -d # start
docker-compose down # stop
docker-compose ps | grep sslibev # status
```
