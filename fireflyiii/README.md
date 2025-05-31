# Home Assistant 插件：fireflyiii

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=%E7%89%88%E6%9C%AC&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=%E6%9E%B6%E6%9E%84&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=%E6%B8%85%E6%9E%90%E4%BB%BB%E5%8A%A1)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=%E6%9E%84%E5%BB%BA)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/%E8%B4%B9%E5%9B%9E%20%E6%88%91%E4%B8%80%E7%A7%8D%E5%8D%96%E5%88%B0%E5%A5%BD%E5%9C%BA%20%28no%20paypal%29-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/%E8%B4%B9%E5%9B%9E%20%E6%88%91%E4%B8%80%E7%A7%8D%E5%8D%96%E5%88%B0%E5%A5%BD%E5%9C%BA%20%E6%88%96%20PayPal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有为我的仓库点亮星星的人！要点亮它，请点击下面的图片，然后在右上角找到它。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/fireflyiii/stats.png)

## 关于

["Firefly III"](https://www.firefly-iii.org) 是一个（自托管的）个人财务管理工具。它可以帮助您跟踪支出和收入，以便更少消费和更多储蓄。
此插件基于 Docker 镜像 https://hub.docker.com/r/fireflyiii/core

## 配置

在首次启动之前，请务必更改您的 APP_KEY！之后您将无法使用，除非重置数据库。

选项可以通过两种方式进行配置：

- 插件选项

```yaml
"CONFIG_LOCATION": config.yaml 的位置 # 设置 config.yaml 的位置（见下文）
"DB_CONNECTION": "list(sqlite_internal|mariadb_addon|mysql|pgsql)" # 定义要使用的数据库类型：sqlite（默认，嵌入在插件中）；MariaDB（如果安装并运行 MariaDB 插件则自动检测），以及需要设置其他 DB_ 字段的外部数据库（mysql 和 pgsql）
"APP_KEY": 32 个字符 # 这是您的加密密钥，切勿丢失！
"DB_HOST": "CHANGEME" # 仅在使用远程数据库时需要
"DB_PORT": "CHANGEME" # 仅在使用远程数据库时需要
"DB_DATABASE": "CHANGEME" # 仅在使用远程数据库时需要
"DB_USERNAME": "CHANGEME" # 仅在使用远程数据库时需要
"DB_PASSWORD": "CHANGEME" # 仅在使用远程数据库时需要
"Updates": hourly|daily|weekly # 设置自动更新
"silent": true # 如果为 false，则显示调试信息
```

- Config.yaml（高级用法）

可以通过按照本指南将附加的变量添加到 config.yaml 中，作为 ENV 变量设置： https://github.com/alexbelgium/hassio-addons/wiki/Add%E2%80%90ons-feature-:-add-env-variables

完整的 ENV 变量列表可以在这里查看：https://raw.githubusercontent.com/firefly-iii/firefly-iii/main/.env.example

## 安装

这个插件的安装非常简单，与安装其他任何插件没有区别。

1. 将我的插件仓库添加到您的 Home Assistant 实例中（在监督管理插件商店右上角，或如果您已配置我的 HA，请单击下面的按钮）
   [![打开您的 Home Assistant 实例并显示添加插件仓库对话框，特定仓库 URL 预填。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击 `保存` 按钮以存储您的配置。
4. 根据您的喜好设置插件选项。
5. 启动插件。
6. 检查插件的日志，看看一切是否正常。
7. 打开 WebUI 并调整软件选项。

## 支持

在 GitHub 上创建问题。

## 插图

![插图](https://raw.githubusercontent.com/firefly-iii/firefly-iii/develop/.github/assets/img/imac-complete.png)

[repository]: https://github.com/alexbelgium/hassio-addons