# Intro

Frp server Dockerfile, customize with frps.init and docker compose.

# Usage

## use docker run directly
```bash
    sudo docker pull dockercat/frps
    # replace with your real config file path
    # replace port with real port your frps use.
    sudo docker run --restart=always -d -v /etc/frp/frps.ini:/etc/frp/frps.ini \
    -p 7000:7000 -p 7001:7001 -p 7500:7500 -p 10080:10080 -p 10443:10443 \
    --name frps dockercat/frps
    sudo docker ps | grep frps
```

## use docker-compose (recommended)

docker-compose.yml

```
version: "3"
services:
  frps:
    restart: always
    volumes:
    # using your real frps.ini file
      - "./frps.ini:/etc/frp/frps.ini"
    ports:
      - "7000:7000"
    #   - "7001:7001"
    #   - "7400:7400"
      - "7500:7500"
    #   - "9122:9122" # for ssh 22
    #   - "9145:9145" # for smb 445
    #   - "9189:9189" # fro rdp 3389
    #   - "10080:10080" # for http
    #   - "10443:10443" # for https
    container_name: frps
    image: dockercat/frps
    # network_mode: "host"
```

```bash
    sudo docker-compose up -d
    sudo docker-compose down
    sudo docker-compose ps
```