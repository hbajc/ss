ARG BUILD_FROM="ghcr.nju.edu.cn/home-assistant/amd64-base"

FROM ${BUILD_FROM} AS final

ENV LANG C.UTF-8

RUN echo "Install base requirements." \
    && apk add --no-cache --virtual .necessary-mjpeg-streamer libjpeg nginx libgphoto2 \
    && echo "Install mjpg-streamer." \
    && apk add --no-cache --virtual .build-dependencies-mjpgstreamer make cmake build-base linux-headers libjpeg-turbo-dev libgphoto2-dev \
    && wget -qO- https://ghfast.top/github.com/jacksonliam/mjpg-streamer/archive/master.tar.gz | tar xz -C /tmp \
    && cd /tmp/mjpg-streamer-master/mjpg-streamer-experimental/ \
    && make --silent \
    && make install --silent \
    && mv www/ /www_mjpg \
    && rm -rf /tmp/mjpg-streamer-master \
    && apk del --no-cache .build-dependencies-mjpgstreamer
COPY rootfs/ /
WORKDIR /

# Make files executable
RUN chmod +x /etc/cont-init.d/*.sh
RUN chmod +x /etc/services.d/*/*
