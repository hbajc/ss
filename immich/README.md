## &#9888; 打开的请求 : [✨ [请求] immich 和 Nextcloud Ingress 支持 (打开于 2025-03-15)](https://github.com/alexbelgium/hassio-addons/issues/1812) 由 [@bessertristan09](https://github.com/bessertristan09)
## &#9888; 打开的问题 : [🐛 [Immich] 面部识别无法使用 (打开于 2025-05-29)](https://github.com/alexbelgium/hassio-addons/issues/1880) 由 [@Marty56](https://github.com/Marty56)
# Home Assistant 插件: immich

⚠️ 该项目正在非常活跃地开发中。预计会有错误和变化。请不要将其作为存储您的照片和视频的唯一方式！(来自开发者)

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20代码%20库)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/给我杯咖啡%20(无%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/给我杯咖啡%20使用%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！如果要加星，请点击下方的图片，然后它会在右上角显示。谢谢！_

[![@alexbelgium/hassio-addons 的星标者仓库名单](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/immich/stats.png)

## 关于

基于网页的文件浏览器。
此插件基于来自 imagegenius 的 [docker 镜像](https://github.com/imagegenius/docker-immich)。

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

此插件的安装相当简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 单击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 仔细配置插件以满足您的偏好，详细信息请参见官方文档。

请注意，您需要安装一个单独的 postgres 插件才能连接数据库。您可以在我的仓库中提前安装 postgres 插件。
请在启动之前更改密码；启动后将无法更改

## 支持

在 GitHub 上创建问题，或在 [Home Assistant 论坛](https://community.home-assistant.io/t/home-assistant-addon-immich/282108/3) 上询问

[repository]: https://github.com/alexbelgium/hassio-addons
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg