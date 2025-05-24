## &#9888; 开放请求 : [✨ [请求] Immich 框架 (开放于 2025-02-13)](https://github.com/alexbelgium/hassio-addons/issues/1764) 由 [@NickBootOne](https://github.com/NickBootOne)
## &#9888; 开放请求 : [✨ [请求] immich 和 Nextcloud Ingress 支持 (开放于 2025-03-15)](https://github.com/alexbelgium/hassio-addons/issues/1812) 由 [@bessertristan09](https://github.com/bessertristan09)
# Home Assistant 插件: immich

⚠️ 该项目正在积极开发中。请期待出现bug和更改。请勿将其作为存储照片和视频的唯一方法！（来自开发者）

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点星的人！要点星，请点击下面的图片，然后在右上角点击。谢谢！_

[![@alexbelgium/hassio-addons 的星图](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/immich/stats.png)

## 关于

基于网页的文件浏览器。
该插件基于 [docker 镜像](https://github.com/imagegenius/docker-immich) 来自 imagegenius。

## 配置

Postgresql 可以是内部或外部的

```yaml
    "PGID": "int",
    "PUID": "int",
    "TZ": "str?",
    "cifsdomain": "str?",
    "cifspassword": "str?",
    "cifsusername": "str?",
    "data_location": "str",
    "localdisks": "str?",
    "networkdisks": "str?",
    "DB_HOSTNAME": "str?",
    "DB_USERNAME": "str?",
    "DB_PORT": "int?",
    "DB_PASSWORD": "str?",
    "DB_DATABASE_NAME": "str?",
    "JWT_SECRET": "str?"
```

## 安装

该插件的安装过程非常简单，与安装其他 Hass.io 插件没有什么不同。

1. [将我的 Hass.io 插件库][repository] 添加到你的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以存储你的配置。
1. 启动该插件。
1. 检查插件的日志以查看一切是否顺利。
1. 仔细根据你的偏好配置插件，具体请参见官方文档。

请注意，你需要安装一个单独的 postgres 插件，以便连接到数据库。你可以在我的库中安装 postgres 插件。
请在启动前更改密码；启动后无法更改。

## 支持

在 GitHub 上创建一个问题，或在 [home assistant 讨论区](https://community.home-assistant.io/t/home-assistant-addon-immich/282108/3) 中询问

[repository]: https://github.com/alexbelgium/hassio-addons
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg