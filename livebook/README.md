# Home assistant 插件：Livebook

Livebook 是一个用于编写互动和协作代码笔记本的网络应用程序

_感谢所有给我的仓库点 star 的人！要点 star，请点击下方的图片，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker 镜像](https://github.com/livebook-dev/livebook)。

## 安装

此插件的安装非常简单，与安装其他 Hass.io 插件没有什么不同。

1. [将我的 Hass.io 插件库][repository]添加到您的 Hass.io 实例。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 打开 WebUI 应该通过 <your-ip>:port 工作。
1. 数据将存储在 /addon_configs/2effc9b9_livebook 中。

## 配置

```
port : 8080 #您希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons