# Home Assistant Community Add-on: pterodactyl Wings (Daemon)
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![项目维护][maintenance-shield]

pterodactyl Wings (Daemon) 游戏服务器适用于 Homeassistant 操作系统

![Ingress 支持](../_images/pterodactyl/ingress.png)

## 关于

Pterodactyl® 是一个免费的开源游戏服务器管理面板，使用 PHP、React 和 Go 构建。Pterodactyl 以安全为设计理念，在隔离的 Docker 容器中运行所有游戏服务器，同时向最终用户提供美观且直观的用户界面。<br />
不要再将就了。让游戏服务器成为您平台上的一等公民。

## 安装

[![FaserF Homeassistant 插件](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
这个插件的安装非常简单，与安装其他自定义 Home Assistant 插件没有区别。<br />
只需点击上述链接或将我的库添加到 Hassio 插件库： <https://github.com/FaserF/hassio-addons>

在安装这个插件之前，必须先安装 MariaDB 集成！

## 配置

**注意**：_更改配置时，请记得重启插件。_

示例插件配置：

```yaml
config_file: /share/path/to/config.yml
```
<br />

**注意**：_这只是一个示例，不要复制粘贴！创建自己的配置！_

### 选项：`config_file`

此选项是必需的。您的 config.yml 文件的路径。

**注意**：_该文件必须存储在 `/share/` 文件夹中的某个位置_

## Ingress

该插件将支持 Homeassistant Ingress。目前仍在开发中！

## 支持

有问题或疑问？

您可以 [在这里打开问题][issue] GitHub。
请记住，这个软件仅在 Raspberry Pi 4 上的 armv7 下进行了测试。

## 作者和贡献者

原程序来自 pterodactyl 项目。有关更多信息，请访问此页面： <https://pterodactyl.io/>
该 hassio 插件由 [FaserF] 贡献。

## 许可证

MIT 许可证

版权 (c) 2019-2022 FaserF & pterodactyl 项目

特此免费授予任何获得此软件及相关文档文件 (以下称 “软件”) 副本的人，在不受限制的情况下处理该软件，包括但不限于以下权利：使用、复制、修改、合并、出版、分发、再许可和/或出售该软件的副本，并允许向其提供该软件的人这样做，前提是满足以下条件：

上述版权声明和本许可声明必须包含在所有副本或软件的重大部分中。

该软件是“按原样”提供的，没有任何形式的担保，明示或暗示，包括但不限于对适销性、特定用途适用性及非侵权的担保。在任何情况下，作者或版权持有人均不对因使用本软件或基于软件的使用或其他交易而产生的任何索赔、损害或其他责任承担责任，无论是在合同诉讼、侵权或其他方面。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[FaserF]: https://github.com/FaserF/
[issue]: https://github.com/FaserF/hassio-addons/issues