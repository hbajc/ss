# 家庭助手插件：Navidrome

[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)
[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%navidrome%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%navidrome%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%navidrome%2Fconfig.json)

[![Codacy 勋章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20Paypal-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！要给项目加星，请点击下面的图片，然后在右上角查看。谢谢！_

[![星标者对 @alexbelgium/hassio-addons 的贡献](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/navidrome/stats.png)

## 关于

各种调整和配置选项的添加。
该插件基于 [docker 镜像](https://hub.docker.com/r/deluan/navidrome)。

## 配置

请参见 https://www.navidrome.org/docs/usage/configuration-options/#available-options

```yaml
    "base_url": "localhost",         # 配置 Navidrome 通过代理访问的基础 URL
    "music_folder": "/data/music",   # 存储音乐库的文件夹，可以为只读
    "data_folder": "/data/data",     # 存储应用数据（数据库）的文件夹
    "log_level": "info",             # 日志级别。用于故障排除。可能的值：error, warn, info, debug, trace
    "certfile": "fullchain.pem",     # TLS 证书的路径
    "keyfile": "privkey.pem",        # TLS 密钥文件的路径
    "ssl": false                     # 应用是否应该使用 https
```

Webui 可以在 `<你的-ip>:端口` 找到。

## 安装

安装该插件非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到你的 Hass.io 实例。
1. 安装该插件。
1. 点击 `保存` 按钮以存储配置。
1. 启动插件。
1. 检查插件日志以查看一切是否正常。
1. 访问 webui，初始化应用程序。
1. 重新启动插件，以应用任何应该应用的选项。

[repository]: https://github.com/alexbelgium/hassio-addons