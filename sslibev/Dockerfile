#
# Dockerfile for shadowsocks-libev
#

FROM alpine
LABEL maintainer="mcxiaoke <docker@mcxiaoke.com>"


ARG LIB_VER=v3.3.5

ENV SERVER_ADDR 0.0.0.0
ENV SERVER_PORT 8388
ENV PASSWORD    shadowsocks
ENV METHOD      chacha20-ietf-poly1305
ENV TIMEOUT     300
ENV DNS_ADDRS    8.8.8.8,8.8.4.4
ENV TZ UTC
ENV ARGS=

RUN set -ex \
 # Change alpinelinux source
 # && sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
 # && echo http://mirrors.ustc.edu.cn/alpine/v3.13/main > /etc/apk/repositories \
 # && echo http://mirrors.ustc.edu.cn/alpine/v3.13/community >> /etc/apk/repositories \
 # Build environment setup
 && apk add --no-cache --virtual .build-deps \
      git \
      autoconf \
      automake \
      build-base \
      c-ares-dev \
      libcap \
      libev-dev \
      libtool \
      libsodium-dev \
      linux-headers \
      mbedtls-dev \
      pcre-dev \
 # Build & install
 && rm -rf /tmp/repo \
 && git clone -b $LIB_VER --recursive --depth 1 https://github.com/shadowsocks/shadowsocks-libev.git /tmp/repo \
 && cd /tmp/repo \
 && ./autogen.sh \
 && ./configure --prefix=/usr --disable-documentation \
 && make install \
 && ls /usr/bin/ss-* | xargs -n1 setcap cap_net_bind_service+ep \
 && apk del .build-deps \
 # Runtime dependencies setup
 && apk add --no-cache \
      ca-certificates \
      rng-tools \
      tzdata \
      $(scanelf --needed --nobanner /usr/bin/ss-* \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u) \
 && rm -rf /tmp/repo

USER nobody

COPY ./entrypoint.sh /entrypoint.sh

CMD /entrypoint.sh
