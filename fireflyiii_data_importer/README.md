# Home Assistant 插件：Fireflyiii 数据导入器

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![Version](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)
![Arch](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ffireflyiii_data_importer%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![Builder](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有为我的仓库点赞的人！要点赞，请点击下面的图片，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![downloads evolution](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/fireflyiii_data_importer/stats.png)

## 关于

["Firefly III"](https://www.firefly-iii.org) 是一款（自托管）个人财务管理工具。它可以帮助你追踪开支和收入，从而帮助你减少支出并增加储蓄。数据导入器旨在帮助你将交易导入 Firefly III。出于安全和维护理由，它与 Firefly III 分开。

此插件基于 Docker 镜像 https://hub.docker.com/r/fireflyiii/data-importer

## 配置

请阅读官方文档以了解如何设置变量： https://docs.firefly-iii.org/data-importer。

配置可以根据 https://docs.firefly-iii.org/data-importer/help/config/ 添加到 /addon_configs/xxx-fireflyiii_data_importer/configurations 文件夹中。

可以通过在 /addon_configs/xxx-fireflyiii_data_importer/import_files 中添加文件来进行自动导入，具体可参考： https://docs.firefly-iii.org/data-importer/usage/command_line/

可以通过两种方式配置选项：

- 插件选项

```yaml
"CONFIG_LOCATION": config.yaml 的位置 # 设置 config.yaml 的位置（见下文）
"FIREFLY_III_ACCESS_TOKEN": 访问 Firefly 所需
"FIREFLY_III_CLIENT_ID": 访问 Firefly 的替代方式
"FIREFLY_III_URL": 你的 URL，可以是本地（docker IP）或外部（公网 IP）
"NORDIGEN_ID": 你的 Nordigen 客户端 ID
"NORDIGEN_KEY": 你的 Nordigen 客户端密钥
"SPECTRE_APP_ID": 你的 Spectre / Salt Edge 客户端 ID
"SPECTRE_SECRET": 你的 Spectre / Salt Edge 客户端密钥
"Updates": hourly|daily|weekly # 设置在 /config/addons_config/fireflyiii_data_importer/import_files 中自动上传文件
"silent": true # 抑制调试消息
```

- Config.yaml（高级用法）

可以通过在配置选项中定义的位置的 config.yaml 中添加它们，将其他变量设置为 ENV 变量，具体可参考此指南： https://github.com/alexbelgium/hassio-addons/wiki/Add%E2%80%90ons-feature-:-add-env-variables

ENV 变量的完整列表可以在这里查看： https://github.com/firefly-iii/data-importer/blob/main/.env.example

## 安装

此插件的安装非常简单，与安装任何其他插件没有区别。

1. 将我的插件库添加到你的 Home Assistant 实例（在左上角的监督 addons 商店，或者如果你已经配置了我的 HA，可以单击下面的按钮）
   [![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 单击 `Save` 按钮以保存你的配置。
1. 根据你的偏好设置插件选项。
1. 启动插件。
1. 检查插件的日志以查看一切是否正常。
1. 打开 webUI 并调整软件选项。

## 支持

在 GitHub 上创建一个问题。

## 插图

[repository]: https://github.com/alexbelgium/hassio-addons