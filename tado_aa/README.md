# Home Assistant 社区插件：Tado 自动辅助地理围栏和开窗检测
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield]
![项目维护][maintenance-shield]

Tado 自动辅助地理围栏和开窗检测，适用于 Homeassistant OS

## 关于

一个 Python 脚本，根据你在 Tado 应用中的设置，自动调整你家中的温度，以及在 Tado TRV 检测到开窗时自动关闭加热（激活开窗模式）。

## 安装

[![FaserF Homeassistant 插件](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
这个插件的安装相当简单，与安装其他自定义 Home Assistant 插件没有什么不同。<br />
只需点击上面的链接或将我的库添加到 hassio 插件库：<https://github.com/FaserF/hassio-addons>

## 配置

**注意**：_请记得在更改配置后重新启动插件。_

示例插件配置：

```yaml
username: my@email.com
password: mySecretPassword
minTemp: 5
maxTemp: 25
```

**注意**：_这只是一个示例，不要复制粘贴！创建你自己的！_

### 选项：`username`

定义你的 Tado 用户名（通常是你的电子邮件地址）。

### 选项：`password`

定义你的 Tado 密码。

### 选项：`minTemp`

定义 Tado 应该设置的最小温度。（可选）

### 选项：`maxTemp`

定义 Tado 应该设置的最高温度。（可选）

## 支持

有问题或疑问？

你可以在这里 [打开问题][issue] GitHub。
请记住，此软件仅在 Raspberry Pi 4 上运行的 armv7 上进行测试。

## 作者与贡献者

原始程序来自 [adrianslabu]。如需更多信息，请访问此页面：<https://github.com/adrianslabu/tado_aa>
这个 hassio 插件由 [FaserF] 提供。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[FaserF]: https://github.com/FaserF/
[issue]: https://github.com/FaserF/hassio-addons/issues
[adrianslabu]: https://github.com/adrianslabu