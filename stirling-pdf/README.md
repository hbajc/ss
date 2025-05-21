# 家庭助理插件：Stirling-pdf

这是一个强大、基于Docker的本地托管网页PDF处理工具。它允许您对PDF文件进行各种操作，包括分割、合并、转换、重新组织、添加图像、旋转、压缩等。这个本地托管的Web应用程序已经发展成为一个全面的功能集，解决了您所有的PDF需求。

Stirling PDF不会发起任何外呼以进行记录保存或跟踪目的。

所有文件和PDF都仅存在于客户端，或在任务执行期间仅驻留在服务器内存中，或临时存在于文件中以仅供任务执行。用户下载的任何文件在此时将已被从服务器中删除。

有点占用内存。

_感谢所有给我的仓库点过星的人！要点星，请点击下面的图片，然后它会在右上角显示。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker镜像](https://github.com/Stirling-Tools/Stirling-PDF)。

## 安装

这个插件的安装非常简单，与安装任何其他Hass.io插件没有不同。

1. [将我的Hass.io插件仓库][repository]添加到您的Hass.io实例。
1. 安装这个插件。750 MB的镜像下载会花费一些时间。
1. 点击`保存`按钮以存储您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. WebUI应该可以通过<your-ip>:port访问。
1. 设置将在 /addon_configs/2effc9b9_stirling-pdf 中。
1. 停止插件，编辑 settings.yaml 文件以更改您需要的任何内容。

## 配置

```
port : 8080 #您希望运行的端口。
```

Webui可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons