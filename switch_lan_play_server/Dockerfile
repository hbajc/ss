ARG BUILD_FROM
# hadolint ignore=DL3006
FROM ${BUILD_FROM}

# Install requirements for add-on
RUN apk -U --no-cache add libpcap-dev
RUN apk -U --no-cache add libuv-dev
RUN apk -U --no-cache add git
RUN apk -U --no-cache add g++
RUN apk -U --no-cache add npm
RUN apk -U --no-cache add nano
RUN apk -U --no-cache add screen
RUN apk -U --no-cache add build-base

#Install SLP
RUN git clone https://ghfast.top/github.com/spacemeowx2/switch-lan-play.git \
    && cd switch-lan-play/server \
    && npm install \
    && npm run build

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]