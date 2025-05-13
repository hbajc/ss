# Home Assistant Community Add-on: Matterbridge
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield]
![项目维护][maintenance-shield]

Homeassistant OS 的 Matterbridge

## 关于

一个简单的聊天桥<br />
让人们能待在自己想待的地方。<br />
在不断增长的协议之间架起桥梁。<br />

## 安装

[![FaserF Homeassistant 添加项](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
此插件的安装非常简单，与安装任何其他自定义 Home Assistant 插件并无不同。<br />
只需点击上面的链接，或将我的仓库添加到 hassio 插件库中： <https://github.com/FaserF/hassio-addons>

将您的网站文件放到 /share/htdocs<br />
您的 index.html 文件应放在的示例文件路径是： /share/htdocs/index.html <br />

如果您希望将您的网站与 mariadb 数据库集成，请确保已经安装了 MariaDB 插件！

## 配置

**注意**：_更改配置后请记得重启插件。_

插件配置示例：

```yaml
config_path: /share/matterbridge.toml
```

**注意**：_这只是一个示例，不要直接复制粘贴！创建您自己的！_

### 选项： `config_path`

您的 matterbridge 配置文件的路径。请查看这里的配置示例： <https://github.com/42wim/matterbridge/blob/master/matterbridge.toml.sample>

**注意**：_它必须放在 /share 目录中的某个位置！_

## 支持

有问题或疑问？

您可以在这里 [提交问题][issue] GitHub。
请记住，此软件仅在 Raspberry Pi 4 上的 armv7 上进行了测试。

## 作者与贡献者

原始程序来自 42wim。如需更多信息，请访问此页面： <https://github.com/42wim/matterbridge><br />
该 hassio 插件由 [FaserF] 提供。

## 许可

MIT 许可

版权 (c) 2019-2022 FaserF & 42wim

特此授予任何获得本软件及相关文档文件（"软件"）副本的人免费许可，不受限制地处理软件，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或销售软件的副本，并允许提供软件的人这样做，前提是满足以下条件：

上述版权声明和本许可声明应包含在所有软件的副本或实质性部分中。

软件是按“原样”提供的，没有任何形式的保证，无论是明确的还是暗示的，包括但不限于对适销性、特定用途的适用性及不侵权的保证。在任何情况下，作者或版权持有人对于任何索赔、损害或其他责任，不论是在合同、侵权或其他方面，均不承担责任，因软件或使用或其他交易所引起的。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[FaserF]: https://github.com/FaserF/
[issue]: https://github.com/FaserF/hassio-addons/issues