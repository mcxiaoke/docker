FROM alpine:latest
LABEL maintainer="docker@mcxiaoke.com"

ENV FRP_VERSION=0.35.1

RUN set -ex && \
    #sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    frp_latest=https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_amd64.tar.gz && \
    frp_file=frp_${FRP_VERSION}_linux_amd64.tar.gz && \
    apk add --no-cache pcre bash && \
    apk add --no-cache --virtual TMP wget tar && \
    mkdir -p /tmp/frp && cd /tmp/frp && \
    wget --no-check-certificate -q ${frp_latest} -O ${frp_file} && tar xzf ${frp_file} && \
    mkdir -p /usr/local/bin && mv frp_${FRP_VERSION}_linux_amd64/frps /usr/local/bin/ && \
    mkdir -p /etc/frp/ && mv frp_${FRP_VERSION}_linux_amd64/frps.ini /etc/frp/ && \
    apk --no-cache del TMP && rm -rf /var/cache/apk/* ~/.cache /tmp/frp/

EXPOSE 7000/tcp 7000/udp 7500/tcp

ENTRYPOINT ["/usr/local/bin/frps", "-c", "/etc/frp/frps.ini"]