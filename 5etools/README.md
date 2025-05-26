# 家庭助手插件: 5etools

一套基于浏览器的 D&D 5e 玩家和 DM 工具。下载的图像来自 5etools GitHub。没有图像或内容托管/发布在 jdeath 的仓库中。由于家庭助手插件创建者不使用此插件，因此不提供支持。自托管的图像可能会比 5etools 网站落后一版。图像大小为 4 GB，因此安装将需要很长时间，请耐心等待。

_感谢所有给我的仓库加星的人！要给它加星，请点击下面的图像，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件使用 [docker 镜像](https://github.com/5etools-mirror-2/5etools-mirror-2.github.io)。

## 安装

安装此插件相当简单，与安装其他 Hass.io 插件没有什么不同。

1. [将我的 Hass.io 插件仓库][repository]添加到你的 Hass.io 实例中。
1. 安装此插件。4 GB 的镜像将需要一些时间下载。
1. 点击 `Save` 按钮以存储配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. WebUI 应该可以通过 ingress 或 <你的-ip>:端口 开放。

## 配置

```
port : 8080 #你想要运行的端口。
```

Webui 可以在 `<你的-ip>:端口` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons