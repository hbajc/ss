# Home Assistant 插件: ConvertX

一个自托管的在线文件转换器。支持831种不同格式。使用TypeScript、Bun和Elysia编写

_感谢所有为我的仓库点赞的人！要点赞，请点击下方图像，然后会在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker 镜像](https://github.com/C4illin/ConvertX)。

## 安装

这个插件的安装非常简单，与安装其他Hass.io插件没有区别。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例中。
1. 安装此插件。 2 GB的镜像下载需要一些时间。
1. 点击 `Save` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. WebUI应该可以通过ingress或 <your-ip>:port 打开。
1. 数据将位于 /addon_configs/2effc9b9_convertx
## 配置

```
port : 3000 #您想要运行的端口。
```

Webui可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons