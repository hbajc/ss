# Hass.io 插件：Tandoor 食谱

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20代码%20基础)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/请我喝杯咖啡%20(没有%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/请我喝杯咖啡%20使用%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库加星的人！要给它加星，请点击下方的图片，然后它将位于右上角。谢谢！_

[![星标者仓库列表 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载发展](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/tandoor_recipes/stats.png)

## 关于

[Tandoor 食谱](https://github.com/TandoorRecipes/recipes)，由 [vabene1111](https://github.com/vabene1111) 制作，旨在帮助有一系列食谱的人分享给家人和朋友，或以整齐有序的方式存储食谱。存在基本的权限系统，但此应用程序并不打算作为公共页面运行。

## 配置

Ingress 添加： https://community.home-assistant.io/t/ingress-access-for-tandoor-recipes/717859

请查看 Tandoor 食谱文档： https://docs.tandoor.dev/install/docker/

```yaml
必需：
    "ALLOWED_HOSTS": "您的系统 URL", # 您需要输入您的 homeassistant URLs（用逗号分隔，无空格）以允许 ingress 工作
    "DB_TYPE": "list(sqlite|postgresql_external)" # 要使用的数据库类型。
    "SECRET_KEY": "str", # 您的秘密密钥
    "PORT": 9928 # 默认情况下，webui 可在 http://HAurl:9928 上使用。如果您需要更改端口，则不应在应用程序内更改，而应仅通过此选项来更改
    "环境": 0|1 # 1 是调试模式，0 是正常模式。除非积极开发，否则应在正常模式下运行。
可选：
    "POSTGRES_HOST": "str?", # 对于 postgresql_external 所需
    "POSTGRES_PORT": "str?", # 对于 postgresql_external 所需
    "POSTGRES_USER": "str?", # 对于 postgresql_external 所需
    "POSTGRES_PASSWORD": "str?", # 对于 postgresql_external 所需
    "POSTGRES_DB": "str?" # 对于 postgresql_external 所需
```

## 安装

这个插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 单击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 小心地根据您的偏好配置插件，具体请参见官方文档。

## 支持

如果您在安装中遇到问题，请确保查看 GitHub。

## 截图

![图像](https://github.com/TandoorRecipes/recipes/raw/develop/docs/preview.png)

[repository]: https://github.com/alexbelgium/hassio-addons

## 外部食谱文件
目录 /config/addons_config/tandoor_recipes/externalfiles 可用于将外部文件导入 Tandoor。您可以在 Docker 内将其映射为 /opt/recipes/externalfiles。
按照此处的说明： https://docs.tandoor.dev/features/external_recipes/