# Home Assistant Community Add-on: Nintendo Switch LAN-Play Client
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]
![项目维护][maintenance-shield]

用于 Homeassistant OS 的 Nintendo Switch LAN-Play 客户端

![Lan-Play Home Home Assistant 插件](../_images/switch_lan_play/screenshot.png)

## 关于

要在线使用您的 CFW Nintendo Switch，您可以使用此插件 + 一个公共或私有服务器。此插件可以用来停止在桌面电脑/笔记本电脑上运行 lan play 客户端。
这只是客户端软件，而不是服务器软件。要在 Homeassistant OS 上使用 lan-play 服务器，请查看我的另一个插件：<https://github.com/FaserF/hassio-addons/switch_lan_play_server>

此 Docker 镜像将自我编译最新的 lan-play 软件，并根据您的架构运行它。更多信息请参见这里：<https://drive.google.com/file/d/1A_4o8HCAfDBFsePcGL3utG-LfzMUovcx/view>
首次安装可能需要长达 10 分钟，这取决于您的硬件。

## 安装

[![FaserF Homeassistant 插件](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
此插件的安装相当简单，与安装其他自定义 Home Assistant 插件没有区别。<br />
只需点击上面的链接或将我的仓库添加到 hassio 插件库：<https://github.com/FaserF/hassio-addons>

## 配置

**注意**：_更改配置后请记得重启插件。_

示例插件配置：

```yaml
server: switch.lan-play.com:11452
```

**注意**：_这只是一个示例，请不要复制粘贴！请创建您自己的！_

### 选项： `server`

此选项是必需的。请在此处写下您想要连接的服务器及其端口。

**注意**：如果您将其留空，将会出现问题。

## 支持

有问题吗？

您可以在 [GitHub 上打开一个问题][issue]。
请记住，此软件仅在 Raspberry Pi 4 上的 armv7 上进行测试。

## 作者与贡献者

原始程序来自 spacemeowx2。如需更多信息，请访问这个 GitHub：<https://github.com/spacemeowx2/switch-lan-play>
这个 hassio 插件由 [FaserF] 带给您。

## 许可证

MIT 许可证

版权 (c) 2019-2025 FaserF & spacemeowx2

特此免费授予任何获得本软件及相关文档文件（"软件"）副本的人，以无限制地使用软件，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售软件副本的权利，以及允许被提供软件的人这样做，前提是遵守以下条件：

上述版权声明和本许可声明应包含在所有软件副本或实质性部分中。

软件是按“原样”提供的，没有任何种类的明示或暗示担保，包括但不限于适销性、特定用途适应性和非侵权的担保。在任何情况下，作者或版权持有人均不对因使用软件或软件的使用或其他交易而产生的任何索赔、损害或其他责任承担责任，无论是基于合同、侵权或其他方面。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[FaserF]: https://github.com/FaserF/
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/FaserF/hassio-addons/issues
[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg