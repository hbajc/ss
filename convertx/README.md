# Home assistant add-on: ConvertX

一个自托管的在线文件转换器。支持831种不同格式。使用TypeScript、Bun和Elysia编写。

_感谢每一个关注我的仓库的人！要关注，请点击下面的图片，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此附加组件使用 [docker 镜像](https://github.com/C4illin/ConvertX)。

## 安装

此附加组件的安装非常简单，与安装任何其他Hass.io附加组件没有太大区别。

1. [将我的Hass.io附加组件仓库][repository]添加到你的Hass.io实例中。
1. 安装此附加组件。2 GB的镜像下载需要一些时间。
1. 点击`保存`按钮以存储你的配置。
1. 启动附加组件。
1. 检查附加组件的日志，以查看一切是否顺利进行。
1. WebUI 应该可以通过ingress或<your-ip>:port访问。
1. 数据将在 /addon_configs/2effc9b9_convertx 中。

## 配置

```
port : 3000 #你希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons