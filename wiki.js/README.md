# Home Assistant Community Add-on: Wiki.js
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield]
![项目维护][maintenance-shield]

Wiki.js 适用于 Homeassistant OS

## 关于

功能强大且可扩展的开源 Wiki 软件。
通过 Wiki.js 美丽直观的界面，使编写文档成为一种乐趣！

## 安装

[![FaserF Homeassistant 插件](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
该插件的安装相当简单，与安装其他自定义 Home Assistant 插件没有区别。<br />
只需点击上面的链接或将我的仓库添加到 hassio 插件库中：<https://github.com/FaserF/hassio-addons>

请确保 MariaDB 插件已经安装！

## 配置

**注意**：_更改配置后，请记得重启插件。_

插件配置示例：

```yaml
ssl: true
certfile: fullchain.pem
keyfile: privkey.pem
```

**注意**：_这只是一个示例，请勿复制粘贴！创建您自己的！_

### 选项：`ssl`

在 web 界面上启用/禁用 SSL (HTTPS)。设置为 `true` 以启用，设置为 `false` 则禁用。

如果您需要自签名证书，请查看我的 openssl 插件：<https://github.com/FaserF/hassio-addons/tree/master/openssl>

**注意**：_文件必须存储在 `/ssl/` 中，这是默认位置_

### 选项：`reset_database`

启用此选项以重置 pterodactyl 的数据库文件。请注意，此操作无法撤消！请谨慎使用。

## Ingress

该插件目前不完全支持 ingress！希望这很快会实现。

## 支持

有问题或疑问？

您可以在此处 [提交问题][issue] 到 GitHub。
请记住，该软件仅在运行于 Raspberry Pi 4 的 armv7 上进行了测试。

## 作者与贡献者

原始程序来自 Requarks 团队 [NGPixel][NGPixel]。有关更多信息，请访问此页面：<https://github.com/Requarks/wiki>
hassio 插件由 [FaserF] 带给您。

## 许可证

MIT 许可证

版权所有 (c) 2023 FaserF & Requarks

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人，不受限制地处理软件，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或出售软件副本的权利，并允许提供软件的人员这样做，遵循以下条件：

上述版权声明和此许可声明应包含在软件的所有副本或重要部分中。

该软件按“原样”提供，不作任何种类的保证，无论是明示或暗示，包括但不限于对适销性、特定用途的适用性和不侵权的保证。在任何情况下，作者或版权持有人均不对因使用或其他交易而产生的任何索赔、损害或其他责任承担责任，无论是因合同、侵权或其他原因。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[FaserF]: https://github.com/FaserF/
[issue]: https://github.com/FaserF/hassio-addons/issues
[NGPixel]: https://github.com/NGPixel