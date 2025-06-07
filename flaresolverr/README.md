# Home assistant 插件：Flaresolver

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fflaresolverr%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fflaresolverr%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fflaresolverr%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢每一个给我的仓库点星的人！要点星，请点击下方的图片，然后它将显示在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载增长](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/flaresolverr/stats.png)

## 关于

FlareSolverr 启动一个代理服务器，并在空闲状态下等待用户请求，使用较少的资源。当请求到达时，它使用 puppeteer 搭配 stealth 插件创建一个无头浏览器（Firefox）。它打开带有用户参数的 URL，并等待 Cloudflare 挑战解决（或超时）。HTML 代码和 Cookies 被返回给用户，这些 Cookies 可以用于通过其他 HTTP 客户端绕过 Cloudflare。

注意：网页浏览器消耗大量内存。如果你在内存有限的机器上运行 FlareSolverr，请勿同时发起多个请求。每次请求都会启动一个新的浏览器。

项目主页： https://github.com/FlareSolverr/FlareSolverr

基于的 docker 镜像： https://hub.docker.com/r/flaresolverr/flaresolverr

## 配置

Webui 可以在 <http://homeassistant:port> 找到

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有不同。

1. [将我的 Hass.io 插件库][repository] 添加到你的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以存储您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 根据你的偏好仔细配置插件，详细信息请参见官方文档。

## 支持

在 GitHub 上创建一个问题

[repository]: https://github.com/alexbelgium/hassio-addons