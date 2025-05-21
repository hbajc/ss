# 家庭助理插件：n8n

n8n 是一个可扩展的工作流自动化工具。通过公平代码分发模型，n8n 将始终拥有可见的源代码，支持自托管，并允许您添加自己的自定义函数、逻辑和应用程序。n8n 的基于节点的方法使其具有高度的灵活性，能够将任何东西连接到一切。

功能未经过测试，但插件可以运行

_感谢所有给我的仓库加星的人！要加星，请点击下面的图片，然后它将出现在右上角。谢谢！_

[![为 @jdeath/homeassistant-addons 的 Stargazers 仓库列表](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker 镜像](https://github.com/n8n-io/n8n)。

## 安装

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例中。
2. 点击 `保存` 按钮以存储您的配置。
3. 启动插件。
4. 插件将会失败，这没关系。
5. SSH 进入您的 homeassistant 并运行 `chmod 2777 /addon_configs/2effc9b9_n8n`。
6. 启动插件。
7. 检查插件的日志以查看一切是否顺利。
8. 打开 WebUI 应该可以通过 `<your-ip>:port` 访问。
9. 设置管理员账户。
10. 设置将保存在 /addon_configs/2effc9b9_n8n 中。

## 配置

```
port : 5678 #您希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons