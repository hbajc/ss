# 家庭助手插件：无界 Chrome

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbrowserless_chrome%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbrowserless_chrome%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbrowserless_chrome%2Fconfig.json)

[![Codacy徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub超级检查器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20代码%20库)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/请%20给我一杯%20咖啡%20(没有%20PayPal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/请%20给我一杯%20咖啡%20通过%20PayPal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有为我的仓库加星的人！要为它加星，请点击以下图片，然后它将出现在右上方。谢谢！_

[![@alexbelgium/hassio-addons的加星者](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/browserless_chrome/stats.png)

## 关于

---

[无界 Chrome](https://github.com/browserless/chrome) 是一个网络服务，允许远程客户端连接、驱动和执行无界作业。
此插件基于 Docker 镜像 https://hub.docker.com/r/browserless/chrome/

## 配置
---

Webui 可以在 <http://homeassistant:PORT> 找到。
可以通过应用程序 webUI 进行配置，除了以下选项

```yaml

```

## 安装

---

安装此插件非常简单，与安装任何其他插件没有不同。

1. 将我的插件库添加到您的 Home Assistant 实例中（在监督者插件商店右上角，或者如果您已配置了我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加插件库对话框，特定仓库 URL 预填。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击 `保存` 按钮以存储您的配置。
1. 根据您的偏好设置选项。
1. 启动插件。
1. 检查插件的日志，以查看一切是否正常。
1. 打开 webUI 并调整软件选项

## 支持

在 GitHub 上创建问题。