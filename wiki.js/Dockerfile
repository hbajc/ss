ARG BUILD_FROM
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Setup base
RUN apk add --no-cache wget tar mariadb-client

ENV NODE_VERSION 22.9.0

# Separate steps for better debugging
RUN addgroup -g 1000 node && \
    adduser -u 1000 -G node -s /bin/sh -D node && \
    apk add --no-cache libstdc++ && \
    apk add --no-cache --virtual .build-deps curl

# Architecture detection and checksum verification
RUN ARCH= && alpineArch="$(apk --print-arch)" && \
    case "${alpineArch##*-}" in \
        x86_64) \
          ARCH='x64' \
          CHECKSUM="6966b7e2e62a6c2f9d096697af980d02b83d92e23a68463f28f8fec9b408d093" \
          ;; \
        *) \
          echo "Unsupported architecture"; exit 1 ;; \
    esac && \
    if [ -n "${CHECKSUM}" ]; then \
        set -eu; \
        curl -fsSLO --compressed "https://unofficial-builds.nodejs.org/download/release/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH-musl.tar.xz"; \
        echo "$CHECKSUM  node-v$NODE_VERSION-linux-$ARCH-musl.tar.xz" | sha256sum -c - || exit 1; \
        tar -xJf "node-v$NODE_VERSION-linux-$ARCH-musl.tar.xz" -C /usr/local --strip-components=1 --no-same-owner; \
        ln -s /usr/local/bin/node /usr/local/bin/nodejs; \
    else \
        echo "Building from source"; \
        apk add --no-cache --virtual .build-deps-full binutils-gold g++ gcc gnupg libgcc linux-headers make python3; \
        export GNUPGHOME="$(mktemp -d)"; \
        for key in \
            4ED778F539E3634C779C87C6D7062848A1AB005C \
            141F07595B7B3FFE74309A937405533BE57C7D57 \
            74F12602B6F1C4E913FAA37AD3A89613643B6201 \
            DD792F5973C6DE52C432CBDAC77ABFA00DDBF2B7 \
            61FC681DFB92A079F1685E77973F295594EC4689 \
            8FCCA13FEF1D0C2E91008E09770F7A9A5AE15600 \
            C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
            890C08DB8579162FEE0DF9DB8BEAB4DFCF555EF4 \
            C82FA3AE1CBEDC6BE46B9360C43CEC45C17AB93C \
            108F52B48DB57BB0CC439B2997B01419BD92F80A; \
        do \
            gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys "$key" || \
            gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key"; \
        done; \
        curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz"; \
        curl -fsSLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc"; \
        gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc; \
        gpgconf --kill all; \
        rm -rf "$GNUPGHOME"; \
        grep " node-v$NODE_VERSION.tar.xz\$" SHASUMS256.txt | sha256sum -c - || exit 1; \
        tar -xf "node-v$NODE_VERSION.tar.xz"; \
        cd "node-v$NODE_VERSION"; \
        ./configure; \
        make -j$(getconf _NPROCESSORS_ONLN) V=; \
        make install; \
        apk del .build-deps-full; \
        cd ..; \
        rm -Rf "node-v$NODE_VERSION"; \
        rm "node-v$NODE_VERSION.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt; \
    fi

RUN rm -f "node-v$NODE_VERSION-linux-$ARCH-musl.tar.xz" && \
    apk del .build-deps && \
    node --version && \
    npm --version

ENV YARN_VERSION 1.22.22

# Separate steps for better debugging
RUN apk add --no-cache --virtual .build-deps-yarn curl gnupg tar

RUN export GNUPGHOME="$(mktemp -d)" && \
    for key in \
        6A010C5166006599AA17F08146C2130DFD2497F5; \
    do \
        gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys "$key" || \
        gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key"; \
    done && \
    curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" && \
    curl -fsSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" && \
    gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz && \
    gpgconf --kill all && \
    rm -rf "$GNUPGHOME" && \
    mkdir -p /opt && \
    tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ && \
    ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn && \
    ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg && \
    rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz && \
    apk del .build-deps-yarn && \
    yarn --version

WORKDIR /wiki
ARG WIKIJS_VERSION="v2.5.303"
RUN wget https://ghfast.top/github.com/Requarks/wiki/releases/download/${WIKIJS_VERSION}/wiki-js.tar.gz && \
    tar xzf wiki-js.tar.gz -C /wiki && \
    rm wiki-js.tar.gz && \
    rm /wiki/config.sample.yml

COPY run.sh /
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]
