# Home Assistant 插件：Livebook

Livebook 是一个用于编写交互式和协作代码笔记本的 web 应用程序

_感谢所有给我的仓库加星的人！要加星，请点击下面的图片，然后在右上角可以看到。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker 镜像](https://github.com/livebook-dev/livebook)。

## 安装

此插件的安装非常简单，和安装其他 Hass.io 插件没有什么不同。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 点击 `Save` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 打开 WebUI 应该可以通过 <your-ip>:port 访问。
1. 数据将位于 /addon_configs/2effc9b9_livebook。
## 配置

```
port : 8080 #您希望运行的端口。
```

WebUI 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons