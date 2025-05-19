# Home assistant 插件：linkding

## 介绍
linkding 是一个您可以自己托管的书签管理器。
它的设计简约、快速，并且易于通过 Docker 设置。

这个名字来源于：
- *link*，在日常语言中通常用作 URL 和书签的同义词
- *Ding* 是德语中的“东西”
- …所以基本上是管理您链接的某种工具

**功能概述：**
- 针对可读性优化的干净用户界面
- 使用标签组织书签
- 批量编辑、Markdown 笔记、稍后阅读功能
- 与其他用户或访客共享书签
- 自动提供书签网站的标题、描述和图标
- 自动存档网站，可以作为本地 HTML 文件或在 Internet Archive 上
- 以 Netscape HTML 格式导入和导出书签
- 可安装为渐进式 Web 应用 (PWA)
- 可用于 [Firefox](https://addons.mozilla.org/firefox/addon/linkding-extension/) 和 [Chrome](https://chrome.google.com/webstore/detail/linkding-extension/beakmhbijpdhipnjhnclmhgjlddhidpe) 的扩展，以及书签小工具
- 通过 OIDC 或认证代理支持单点登录 (SSO)
- 用于开发第三方应用的 REST API
- 用户自助服务和原始数据访问的管理面板

_感谢所有给我的代码库加星的人！要加星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

该插件使用 [docker 镜像](https://github.com/sissbruecker/linkding)。

有点占内存。它使用常规的 linkding 镜像，而不是 plus 版本。如果您想使用 plus 版本，请下载插件源代码，放置在 /addons/ 下，编辑 config.json，将版本更改为 latest-plus，而不是版本号。

## 安装

该插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 单击 `Save` 按钮以存储您的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. WebUI 应该可以通过 <your-ip>:port 访问。
1. 设置将位于 /addon_configs/2effc9b9_linkding
1. 停止插件，编辑 settings.yaml 文件以更改您需要的任何内容

## 配置
1. 您必须创建初始超级用户账户。
1. 启动插件
1. 登录 homeassistant cli
1. `docker ps | grep "link"`，复制第一个显示的十六进制字符串
1. docker exec -it 3c32b108bd10 python manage.py createsuperuser --username=joe --email=joe@mail.com
1. 输入密码，然后重启插件
```
port : 9090 #您想运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons