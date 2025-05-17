# Home Assistant Community Add-on: pterodactyl Wings (Daemon)
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![项目维护][maintenance-shield]

pterodactyl Wings (Daemon) 游戏服务器 for Homeassistant OS

![Ingress 支持](../_images/pterodactyl/ingress.png)

## 关于

Pterodactyl® 是一个免费的开源游戏服务器管理面板，使用 PHP、React 和 Go 构建。考虑到安全性，Pterodactyl 在隔离的 Docker 容器中运行所有游戏服务器，同时为最终用户提供美观且直观的用户界面。<br />
不要再将就了。让游戏服务器成为您平台上的一流公民。

## 安装

[![FaserF Homeassistant Addons](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
此附加组件的安装非常简单，与安装其他自定义 Home Assistant 附加组件没有区别。<br />
只需点击上面的链接或将我的仓库添加到 hassio 附加组件库中： <https://github.com/FaserF/hassio-addons>

在安装这个之前，需要安装 MariaDB 集成！

## 配置

**注意**：_更改配置后，请记得重启附加组件。_

附加组件配置示例：

```yaml
config_file: /share/path/to/config.yml
```
<br />

**注意**：_这只是一个示例，不要复制粘贴！请创建您自己的！_

### 选项： `config_file`

此选项是必需的。指向您的 config.yml 文件的路径。

**注意**：_该文件必须存储在 `/share/` 文件夹内的某个地方_

## Ingress

此附加组件将支持 Homeassistant Ingress。目前仍在开发中！

## 支持

有问题或疑问？

您可以在 [这里打开问题][issue] GitHub。
请记住，此软件仅在 Raspberry Pi 4 上的 armv7 环境中测试。

## 作者与贡献者

原始程序来自 pterodactyl 项目。有关更多信息，请访问此页面： <https://pterodactyl.io/>
该 hassio 附加组件由 [FaserF] 提供。

## 许可证

MIT 许可证

版权 (c) 2019-2025 FaserF & pterodactyl 项目

特此免费授予任何获得本软件及相关文档文件（以下称"软件"）副本的人，无限制地处理软件，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或销售软件副本，以及允许提供软件的人这样做，前提是遵守以下条件：

上述版权声明和本许可声明应包含在所有软件的副本或实质性部分中。

该软件按“原样”提供，不提供任何类型的保证，无论是明示或暗示，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人都不对因使用软件或与软件相关的其他交易而引起的任何索赔、损害或其他责任承担责任，无论是在合约诉讼、侵权诉讼或其他方面。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[FaserF]: https://github.com/FaserF/
[issue]: https://github.com/FaserF/hassio-addons/issues