# 家庭助手附加组件: Livebook

Livebook是一个用于编写交互式和协作代码笔记本的Web应用程序。

_感谢所有给我仓库点赞的人！要点赞，请点击下面的图像，然后它将位于右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此附加组件使用[docker镜像](https://github.com/livebook-dev/livebook)。

## 安装

此附加组件的安装非常简单，与安装任何其他Hass.io附加组件没有区别。

1. [将我的Hass.io附加组件仓库][repository]添加到您的Hass.io实例。
1. 点击`保存`按钮以保存您的配置。
1. 启动附加组件。
1. 检查附加组件的日志以查看一切是否顺利。
1. 打开WebUI应该可以通过<your-ip>:port访问。
1. 数据将在/addon_configs/2effc9b9_livebook中找到。

## 配置

```
port : 8080 #您希望运行的端口。
```

Webui可以在`<your-ip>:port`找到。

[repository]: https://github.com/jdeath/homeassistant-addons