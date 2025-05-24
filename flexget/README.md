# Hass.io 插件：Flexget

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fflexget%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fflexget%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fflexget%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20代码%20基础)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/请给我一杯咖啡%20(无%20PayPal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/请给我一杯咖啡%20使用%20PayPal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有已给我的仓库加星的人！要加星，请点击下面的图像，然后它将显示在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/flexget/stats.png)

## 关于

FlexGet 是一个多用途的媒体自动化工具。查看 https://flexget.com/

默认密码是 'homeassistant123'，或可以从插件选项中设置

## 需求

## 配置

    "PUID": 自定义用户 (默认 root)
    "PGID": 自定义用户 (默认 root)
    "WebuiPass": webui 密码定义
    "FG_PLUGINS": 插件添加
    "FG_LOG_LEVEL": 日志级别 (critical|error|warning|info|verbose|debug|trace)

## 启动

- 启动插件。等待一段时间并检查日志是否有错误。

## 故障排除

如果您的安装出现问题，请确保查看 GitHub。