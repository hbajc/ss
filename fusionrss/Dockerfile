ARG BUILD_FROM
FROM docker.1ms.run/rook1e404/fusion	
	
COPY run.sh /
RUN apt install -y jq
	
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]

### LABELS
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_DESCRIPTION
ARG BUILD_NAME
ARG BUILD_REF
ARG BUILD_REPOSITORY
ARG BUILD_VERSION
LABEL \
    io.hass.name="${BUILD_NAME}" \
    io.hass.description="${BUILD_DESCRIPTION}" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="jdeath (https://ghfast.top/github.com/jdeath)" \
    org.opencontainers.image.title="${BUILD_NAME}" \
    org.opencontainers.image.description="${BUILD_DESCRIPTION}" \
    org.opencontainers.image.vendor="Home Assistant Add-ons" \
    org.opencontainers.image.authors="jdeath (https://ghfast.top/github.com/jdeath)" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://ghfast.top/github.com/jdeath" \
    org.opencontainers.image.source="https://ghfast.top/github.com/${BUILD_REPOSITORY}" \
    org.opencontainers.image.documentation="https://ghfast.top/github.com/${BUILD_REPOSITORY}/blob/main/README.md" \
    org.opencontainers.image.created=${BUILD_DATE} \
    org.opencontainers.image.revision=${BUILD_REF} \
    org.opencontainers.image.version=${BUILD_VERSION}
