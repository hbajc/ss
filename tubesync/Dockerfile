ARG BUILD_FROM
FROM ghcr.nju.edu.cn/meeb/tubesync:latest

VOLUME [ "/config" ]

#RUN sed -i 's/Path('\''\/'\'')/Path('\''\/config\/addons_config\/tubesync'\'')/' /app/tubesync/local_settings.py 
#RUN sed -i 's/DOWNLOADS_BASE_DIR = BASE_DIR/DOWNLOADS_BASE_DIR = \/share\/tubesync/g' /app/tubesync/local_settings.py
#RUN sed -i 's/Path('\''\/'\'')/Path('\''\/config\/addons_config\/tubesync'\'')/' /app/tubesync/local_settings.py 
RUN sed -i 's/DOWNLOADS_BASE_DIR = BASE_DIR/DOWNLOADS_BASE_DIR = \x27\/config\/addons_config\/tubesync\x27/g' /app/tubesync/settings.py 
#RUN sed -i 's/CONFIG_BASE_DIR = BASE_DIR/CONFIG_BASE_DIR = \x27\/config\/addons_config\/tubesync\x27/g' /app/tubesync/settings.py
RUN sed -i 's/MEDIA_ROOT = CONFIG_BASE_DIR \/ \x27media\x27/MEDIA_ROOT = \x27\/config\/addons_config\/tubesync\/media\x27/g' /app/tubesync/settings.py
RUN sed -i 's/DOWNLOAD_ROOT = DOWNLOADS_BASE_DIR \/ \x27downloads\x27/DOWNLOAD_ROOT = \x27\/config\/addons_config\/tubesync\/downloads\x27/g' /app/tubesync/settings.py

#RUN sed -i 's/Path('\''\/'\'')/Path('\''\/config\/addons_config\/tubesync\/'\'')/' /app/tubesync/local_settings.py 
RUN sed -i 's/DOWNLOADS_BASE_DIR = ROOT_DIR \/ \x27downloads\x27/DOWNLOADS_BASE_DIR = \x27\/config\/addons_config\/tubesync\/downloads\x27/g' /app/tubesync/local_settings.py
#RUN sed -i 's/CONFIG_BASE_DIR = ROOT_DIR \/ \x27config\x27/CONFIG_BASE_DIR = \x27\/config\/addons_config\/tubesync\/config\x27/g' /app/tubesync/local_settings.py
#RUN sed -i 's/CONFIG_BASE_DIR = BASE_DIR/CONFIG_BASE_DIR = \x27\/config\/addons_config\/tubesync\x27/g' /app/tubesync/local_settings.py
RUN sed -i 's/MEDIA_ROOT = CONFIG_BASE_DIR \/ \x27media\x27/MEDIA_ROOT = \x27\/config\/addons_config\/tubesync\/media\x27/g' /app/tubesync/local_settings.py
RUN sed -i 's/DOWNLOAD_ROOT = DOWNLOADS_BASE_DIR \/ \x27downloads\x27/DOWNLOAD_ROOT = \x27\/config\/addons_config\/tubesync\/downloads\x27/g' /app/tubesync/local_settings.py
RUN sed -i 's/CONFIG_BASE_DIR \/ \x27db.sqlite3\x27/\x27\/config\/addons_config\/tubesync\/db.sqlite3\x27/g' /app/tubesync/local_settings.py
#RUN sed -i 's/BASE_DIR = Path(__file__).resolve().parent.parent/BASE_DIR =Path('\''\/config\/addons_config\/tubesync'\'')/' /app/tubesync/settings.py
#RUN sed -i 's/BASE_DIR = Path(__file__).resolve().parent.parent/BASE_DIR =Path('\''\/config\/addons_config\/tubesync'\'')/' /app/tubesync/local_settings.py
RUN sed -i 's/YOUTUBE_DL_CACHEDIR = CONFIG_BASE_DIR \/ \x27cache\x27/YOUTUBE_DL_CACHEDIR = \x27\/config\/addons_config\/tubesync\/cache\x27/g' /app/tubesync/local_settings.py
#RUN sed -i 's/COOKIES_FILE = CONFIG_BASE_DIR \/ \x27cookies.txt\x27/COOKIES_FILE = \x27\/config\/addons_config\/tubesync\/cookies.txt\x27/g' /app/tubesync/local_settings.py

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
