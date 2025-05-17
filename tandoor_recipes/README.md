# Hass.io 插件：Tandoor 食谱

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=版本&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=入口&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=架构&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=代码%20审查)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=构建器)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/请%20请我喝杯咖啡%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/请%20请我喝杯咖啡%20通过%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有为我的库加星的人！要加星，请点击下面的图片，然后它会在右上角。谢谢！_

[![星际观察者库名单 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/tandoor_recipes/stats.png)

## 关于

[Tandoor 食谱](https://github.com/TandoorRecipes/recipes)，由 [vabene1111](https://github.com/vabene1111) 制作，旨在为希望与家人和朋友分享或简单地以良好组织的方式存储他们的食谱的人提供服务。存在基本的权限系统，但该应用程序并不打算作为公共页面运行。

## 配置

Ingress 添加 : https://community.home-assistant.io/t/ingress-access-for-tandoor-recipes/717859

请查看 Tandoor 食谱文档 : https://docs.tandoor.dev/install/docker/

```yaml
所需：
    "ALLOWED_HOSTS": "你的系统网址", # 你需要输入你的 homeassistant URL（用逗号分隔，且没有空格）以允许 ingress 工作
    "DB_TYPE": "list(sqlite|postgresql_external)" # 使用的数据库类型。
    "SECRET_KEY": "str", # 你的密钥
    "PORT": 9928 # 默认情况下，webui 在 http://HAurl:9928 可用。如果你需要更改端口，应该只通过这个选项，而不是应用程序内进行。
    "Environment": 0|1 # 1 是调试模式，0 是正常模式。除非积极开发，否则应在正常模式下运行。
可选：
    "POSTGRES_HOST": "str?", # 需要用于 postgresql_external
    "POSTGRES_PORT": "str?", # 需要用于 postgresql_external
    "POSTGRES_USER": "str?", # 需要用于 postgresql_external
    "POSTGRES_PASSWORD": "str?", # 需要用于 postgresql_external
    "POSTGRES_DB": "str?" # 需要用于 postgresql_external
```

## 安装

这个插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到你的 Hass.io 实例。
2. 安装此插件。
3. 点击 `保存` 按钮以存储你的配置。
4. 启动插件。
5. 查看插件的日志以确认一切顺利。
6. 小心配置插件以符合你的偏好，详细信息请参见官方文档。

## 支持

如果你的安装遇到问题，请务必查看 GitHub。

## 截图

![图像](https://github.com/TandoorRecipes/recipes/raw/develop/docs/preview.png)

[repository]: https://github.com/alexbelgium/hassio-addons

## 外部食谱文件
目录 /config/addons_config/tandoor_recipes/externalfiles 可用于将外部文件导入到 Tandoor 中。你可以将其与 Docker 中的 /opt/recipes/externalfiles 映射。
按照这里的指示： https://docs.tandoor.dev/features/external_recipes/