# 家庭助理插件: immich

⚠️ 该项目正在积极开发中。预期会有错误和更改。请勿将其作为存储照片和视频的唯一方法！（来自开发者）

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=%E7%89%88%E6%9C%AC&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fimmich%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub 超级 Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=%E6%8C%87%E5%AE%9A%E4%BF%A1%E7%94%A8%E4%BE%86%E7%B7%A8%E7%94%9F%E4%BF%A1%E7%94%A8%E4%BE%86)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=%E6%9E%84%E5%BB%BA%E5%99%A8)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/%E8%B4%B9%E6%AC%BE%E7%92%B0%E5%93%AA%E7%95%99%E4%B8%80%E8%9B%8B-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/%E8%B4%B9%E6%AC%BE%E7%92%B0%E5%93%AA%E7%95%99%E4%B8%8D%E7%9A%84Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有点赞我的仓库的人！要点赞，请点击下面的图像，然后它会显示在右上角。谢谢！_

[![星标者名单 @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载变化](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/immich/stats.png)

## 关于

基于Web的文件浏览器。
此附加组件基于来自 imagegenius 的 [docker 镜像](https://github.com/imagegenius/docker-immich)。

## 配置

Postgresql 可以是内部或外部

```yaml
    "PGID": "int",
    "PUID": "int",
    "TZ": "str?",
    "cifsdomain": "str?",
    "cifspassword": "str?",
    "cifsusername": "str?",
    "data_location": "str",
    "localdisks": "str?",
    "networkdisks": "str?",
    "DB_HOSTNAME": "str?",
    "DB_USERNAME": "str?",
    "DB_PORT": "int?",
    "DB_PASSWORD": "str?",
    "DB_DATABASE_NAME": "str?",
    "JWT_SECRET": "str?"
```

## 安装

此附加组件的安装非常简单，与安装任何其他 Hass.io 附加组件没有区别。

1. [将我的 Hass.io 附加组件库][repository] 添加到你的 Hass.io 实例。
1. 安装此附加组件。
1. 点击 `保存` 按钮以保存配置。
1. 启动附加组件。
1. 检查附加组件的日志以查看一切是否顺利。
1. 根据自己的偏好仔细配置附加组件，具体请参见官方文档。

请注意，你需要安装一个单独的 postgres 附加组件才能连接数据库。你可以直接在我的仓库中安装 postgres 附加组件。
请确保在启动之前更改密码；启动后将无法更改。

## 支持

在 GitHub 上创建一个问题，或在 [home assistant 论坛](https://community.home-assistant.io/t/home-assistant-addon-immich/282108/3) 上询问。

[repository]: https://github.com/alexbelgium/hassio-addons
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg