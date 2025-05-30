# Home assistant 插件：Postgres

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fpostgres%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有为我的代码库点赞的人！要给我点赞，请点击下面的图像，然后会在右上角显示。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/postgres/stats.png)

## 关于

PostgreSQL，通常简称为 "Postgres"，是一种对象关系数据库管理系统 (ORDBMS)，强调可扩展性和标准兼容性。作为数据库服务器，它的主要功能是存储数据，安全地支持最佳实践，并在其他软件应用程序请求时检索数据，无论是运行在同一台计算机上的应用程序，还是运行在另一台计算机上的网络（包括互联网）。它可以处理从小型单机应用程序到大型互联网面向应用程序的工作负载，允许多个用户并发访问。最近的版本还提供了数据库本身的复制，以增强安全性和可扩展性。

此插件基于官方镜像：https://hub.docker.com/_/postgres

## 配置

Postgres 的默认端口为 5432，并暴露给主机网络。

默认用户：`postgres`
密码：`由 POSTGRES_PASSWORD 设置`

你可以配置以下选项：
```yaml
POSTGRES_PASSWORD
POSTGRES_USER
POSTGRES_DB
POSTGRES_INITDB_ARGS
POSTGRES_HOST_AUTH_METHOD
```
有关更多信息，请查看 [基础镜像文档](https://hub.docker.com/_/postgres)。

默认情况下，`postgresql.conf` 存储在其他插件和 Home Assistant 可访问的卷中，因此你可以方便地通过例如文件编辑器插件进行修改。如果你更喜欢更好的安全性，可以将 `CONFIG_LOCATION` 修改为例如 `/data/orig/postgresql.conf`，这样它将仅对该插件可访问，但你需要通过 [Hassio SSH](https://developers.home-assistant.io/docs/operating-system/debugging/) 进行修改。

## 安装

安装此插件相当简单，与安装其他插件没有不同。

1. 将我的插件库添加到你的 Home Assistant 实例（在监督器插件商店右上角，或者如果你已配置我的 HA，请点击下面的按钮）
   [![打开你的 Home Assistant 实例，并显示添加插件库对话框，带有特定的库 URL 预填。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 单击 `保存` 按钮以存储配置。
4. 根据你的偏好设置插件选项，至少需要 POSTGRES_PASSWORD。
5. 启动插件。
6. 检查插件的日志以查看一切是否顺利。
7. 使用任何 Postgres 客户端连接，例如连接到 `homeassistant.local:5432`

## 支持

在 GitHub 上创建一个问题

[repository]: https://github.com/alexbelgium/hassio-addons