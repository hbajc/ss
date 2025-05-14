# Home Assistant Community Add-on: Nintendo Switch LAN-Play 服务器
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]
![项目维护][maintenance-shield]

Homeassistant OS 的 Nintendo Switch LAN-Play 服务器

## 关于

要在您修改过的 Nintendo Switch 上在线游戏，您可以使用此附加组件 + 一个公共或私人的服务器。此附加组件可以被用来停止在台式电脑/笔记本电脑上运行 LAN Play 客户端。
这只是服务器软件，而不是客户端软件。要在 Homeassistant OS 上使用 LAN-Play 客户端，请查看我的其他附加组件：<https://github.com/FaserF/hassio-addons/switch_lan_play>

此 Docker 镜像将自我编译最新的 LAN-Play 软件，并根据您的架构运行它。更多信息可以在这里找到：<https://drive.google.com/file/d/1A_4o8HCAfDBFsePcGL3utG-LfzMUovcx/view>
首次启动可能需要长达 10 分钟，因为这个！具体取决于您的硬件。

## 安装

[![FaserF Homeassistant Addons](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
此附加组件的安装非常简单，与安装其他自定义 Home Assistant 附加组件没有不同。<br />
只需点击上面的链接或将我的库添加到 hassio 附加组件库：<https://github.com/FaserF/hassio-addons>

## 配置

**注意**：_当配置更改时，请记得重启附加组件。_

附加组件配置示例：

```yaml
username: mysecretuser
password: mysecretpw
```

**注意**：_这只是一个示例，别复制粘贴！创建你自己的！_

### 选项：`username`

此选项是可选的。如果您不设置用户名，则不会使用任何身份验证来连接到您的服务器。

### 选项：`password`

此选项是可选的。如果您不设置密码，则不会使用任何身份验证来连接到您的服务器。

**注意**：如果您留空，将会出现问题。

## Homeassistant 传感器
要在您的配置中获取一个 HA 传感器，显示在线人数和服务器版本属性，请在您的 configuration.yaml 中添加以下内容：

```yaml
sensor:
  - platform: rest
    name: Switch LAN-Play 在线
    resource: http://{YOUR_SERVER_IP}:11451/info
    method: GET
    unit_of_measurement: people
    json_attributes:
      - version
    value_template: "{{value_json.online}}"
```

## 支持

有问题吗？

您可以 [在这里打开一个问题][issue] GitHub。
请记住，此软件仅在运行于 Raspberry Pi 4 的 armv7 上进行测试。

## 作者与贡献者

原程序来自 spacemeowx2。欲了解更多信息，请访问此 GitHub：<https://github.com/spacemeowx2/switch-lan-play>
该 hassio 附加组件由 [FaserF] 提供。

## 许可证

MIT 许可证

版权所有 (c) 2019-2023 FaserF 和 spacemeowx2

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人处理软件的权利，不受限制，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或销售软件副本的权利，以及允许提供软件的人这样做，受以下条件的约束：

上述版权声明和本许可声明应包含在所有软件副本或重要部分中。

软件按“原样”提供，不提供任何种类的担保，无论是明示或暗示，包括但不限于对适销性、特定用途的适用性和不侵权的担保。在任何情况下，作者或版权持有人均不对因使用或其他交易引起的任何索赔、损害或其他责任承担责任，无论是在合同诉讼、侵权或其他方面。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[FaserF]: https://github.com/FaserF/
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/FaserF/hassio-addons/issues
[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg