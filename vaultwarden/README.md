# Home assistant 插件: Vaultwarden

Vaultwarden 是使用 Rust 编写的 Bitwarden 服务器 API 的替代实现，兼容上游 Bitwarden 客户端，*非常适合自托管部署，在运行官方资源消耗严重的服务可能不理想的情况下。

这个版本与官方的 Home Assistant 插件以及 Alex Belgium 的插件之间的区别在于，它将数据存储在 /addons_config 中，这使得在意外卸载或升级失败时更容易移动内容。您必须确保使用 Argon 加密的密码，这应该是默认设置。此外，内置的 Home Assistant 版本通常不会更新（即使在多次请求后）。这个插件仅使用官方的 docker 镜像，无任何更改，而其他插件则在镜像中添加了额外的内容。

_感谢所有给我仓库加星的人！要加星，请点击下面的图片，然后在右上角查看。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件使用 [docker 镜像](https://github.com/dani-garcia/vaultwarden)。

## 安装

安装这个插件非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 点击 `Save` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切顺利。
1. 打开 WebUI 应该通过 <your-ip>:port 工作。
1. 您的数据将存储在 /addon-configs/2effc9b9_vaultwarden/

如果您有一个现有的 vaultwarden 安装（默认插件或 alexbelgium 的），
1. 确保我的插件已经运行过一次，但随后请确保停止它。
1. 登录到 Home Assistant CLI。
1. `docker ps | grep "vault"`
1. 找到 docker 容器的 ID。
1. `docker cp CONTAINERID:/data /addon-configs/2effc9b9_vaultwarden/`
1. 然后在 `/addon-configs/2effc9b9_vaultwarden/` 中将 `data` 文件夹中的所有内容移动到 `/addon-configs/2effc9b9_vaultwarden/` 中。
1. 所有文件现在应该在 `/addon-configs/2effc9b9_vaultwarden/` 中。
1. 停止默认插件，关闭“开机启动”。
1. 启动我的插件。
1. 查阅文档进行配置: https://github.com/dani-garcia/vaultwarden


## 配置
1. 一旦设置完成，限制来自您网络外部的管理员控制面板访问。
1. 您可以通过停止容器并编辑 `/addon-configs/2effc9b9_vaultwarden/config.json` 手动配置许多参数。
1. 确保您的 `admin_token` 是 argon2 加密的: https://github.com/dani-garcia/vaultwarden/wiki/Enabling-admin-page#secure-the-admin_token
1. 如果不是，`docker ps | grep "vault"`，前面的数字/字母是容器 ID。
2. `docker exec -it containerID /bin/bash`
3. `cd /` `/vaultwarden hash --preset owasp` 输入一个密码，然后替换管理员令牌。
4. 由于这个文件是可访问的，我想任何人都可以这样做，所以要小心。如果可以访问您的 Home Assistant 机器，这也可以在容器内部完成，因此安全性并没有降低。

```
port : 7277 #您希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons