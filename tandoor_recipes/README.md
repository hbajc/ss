# Hass.io 插件：Tandoor 食谱

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Ftandoor_recipes%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有为我的仓库加星的朋友们！要加星，请点击下面的图像，然后它会在右上方显示。谢谢！_

[![星标用户列表 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/tandoor_recipes/stats.png)

## 关于

[Tandoor 食谱](https://github.com/TandoorRecipes/recipes)，由 [vabene1111](https://github.com/vabene1111) 制作，旨在为有收集食谱的用户提供一个与家人朋友分享或简单地以井然有序的方式存储食谱的平台。虽然基本权限系统是存在的，但该应用程序并不旨在作为公共页面使用。

## 配置

Ingress 添加 ： https://community.home-assistant.io/t/ingress-access-for-tandoor-recipes/717859

请查看 Tandoor 食谱文档 : https://docs.tandoor.dev/install/docker/

```yaml
必需项：
    "ALLOWED_HOSTS": "你的系统网址", # 你需要输入家庭助理的网址（以逗号分隔，无空格）以允许 ingress 工作
    "DB_TYPE": "list(sqlite|postgresql_external)" # 要使用的数据库类型。
    "SECRET_KEY": "str", # 你的密钥
    "PORT": 9928 # 默认情况下，网页用户界面在 http://HAurl:9928 上可用。如果需要更改端口，应该只通过此选项进行更改，而不是在应用中。
    "Environment": 0|1 # 1 是调试模式，0 是正常模式。除非是在主动开发，否则应以正常模式运行。
可选项：
    "POSTGRES_HOST": "str?", # 对于 postgresql_external 所需
    "POSTGRES_PORT": "str?", # 对于 postgresql_external 所需
    "POSTGRES_USER": "str?", # 对于 postgresql_external 所需
    "POSTGRES_PASSWORD": "str?", # 对于 postgresql_external 所需
    "POSTGRES_DB": "str?" # 对于 postgresql_external 所需
```

## 安装

安装此插件非常简单，与安装其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到你的 Hass.io 实例中。
1. 安装此插件。
1. 点击 `保存` 按钮以存储你的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否正常。
1. 仔细配置插件以满足你的偏好，参见官方文档。

## 支持

如果你的安装过程中遇到问题，请务必查看 GitHub。

## 截图

![image](https://github.com/TandoorRecipes/recipes/raw/develop/docs/preview.png)

[repository]: https://github.com/alexbelgium/hassio-addons

## 外部食谱文件
目录 /config/addons_config/tandoor_recipes/externalfiles 可用于将外部文件导入到 Tandoor 中。你可以将其映射到 Docker 中的 /opt/recipes/externalfiles。
有关指引，请参见： https://docs.tandoor.dev/features/external_recipes/