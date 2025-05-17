# Home Assistant Community Add-on: pterodactyl Panel
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![项目维护状态][maintenance-shield]

pterodactyl 面板游戏服务器用于 Homeassistant OS

![Ingress 支持](../_images/pterodactyl/ingress.png)

## 介绍

**警告：目前仅限于有限功能。现在可以认为是测试版和不稳定。如果您的游戏服务器丢失等，请不要责怪我。**
**对我来说，直到现在我都无法登录。似乎与 redis 有关，但我不太明白具体是什么。**

Pterodactyl® 是一个免费、开源的游戏服务器管理面板，使用 PHP、React 和 Go 构建。考虑到安全性，Pterodactyl 在隔离的 Docker 容器中运行所有游戏服务器，同时向最终用户呈现一个美观且直观的 UI。<br />
不要再妥协。让游戏服务器在您的平台上成为一流公民。

## 安装

[![FaserF Homeassistant 插件](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
此插件的安装非常简单，与安装任何其他自定义 Home Assistant 插件没有不同。<br />
只需点击上面的链接或将我的库添加到 hassio 插件库中： <https://github.com/FaserF/hassio-addons>

## 配置

在安装此插件之前，需要 MariaDB 集成！

然后在 MariaDB 插件中创建一个名为“pterodactyl”的新用户，对数据库“panel”具有完全权限。

**注意**：_更改配置时，请记得重启插件。_

示例插件配置：

```yaml
password: your_MariaDB_password
ssl: false
certfile: itdoesntmatter_as_ssl_is_set_to_false
keyfile: itdoesntmatter_as_ssl_is_set_to_false
```
<br />
推荐示例插件配置：

```yaml
password: your_MariaDB_password
ssl: true
certfile: fullchain.pem
keyfile: privkey.pem
```

**注意**：_这只是一个示例，请不要复制和粘贴！请自行创建！_

### 选项：`password`

此选项是必需的。MariaDB “pterodactyl” 用户的密码。

### 选项：`ssl`

在 Web 界面上启用/禁用 SSL（HTTPS）。

如果您需要自签名证书，请查看我的 openssl 插件： <https://github.com/FaserF/hassio-addons/tree/master/openssl>

**注意**：_文件必须存储在 `/ssl/` 中，这是默认设置_

### 选项：`reset_database`

启用重置 pterodactyl 的数据库文件。请注意，此操作无法撤销！请小心使用。

### 选项：`password`

此选项是必需的。您为 pterodactyl 用户定义的 MariaDB 密码。

**注意**：_文件必须存储在 `/share/` 文件夹中的某个位置_

## 默认登录凭证

电子邮件：<admin@example.com>
用户名：admin
密码：选项 `password` 中定义的密码

## Ingress

此插件将支持 Homeassistant Ingress。目前仍在开发中！

## 支持

有问题或疑问？

您可以在这里 [提交问题][issue] GitHub。
请记住，此软件仅在 Raspberry Pi 4 的 armv7 上经过测试。

## 作者与贡献者

原程序来自 pterodactyl 项目。如需更多信息，请访问此页面： <https://pterodactyl.io/>
该 hassio 插件由 [FaserF] 提供。

## 许可证

MIT 许可证

版权所有 (c) 2019-2025 FaserF & pterodactyl 项目

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人使用
该软件的权利，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售
软件副本的权利，并允许向其提供软件的人这样做，受以下条件的限制：

上述版权声明和本许可证声明应包含在所有
软件的副本或实质性部分中。

软件按“原样”提供，不附有任何形式的保修，明确或
暗示，包括但不限于对适销性、
特定用途的适用性和非侵权的担保。在任何情况下，
作者或版权持有者均不对因
使用或其他交易而引起的任何索赔、损害或其他
责任承担责任。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[FaserF]: https://github.com/FaserF/
[issue]: https://github.com/FaserF/hassio-addons/issues