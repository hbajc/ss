# Home Assistant Community Add-on: AdGuard Home

[AdGuard Home][adguard] 是一个网络范围的广告和跟踪器阻止 DNS 服务器，具有家长控制（成人内容阻止）功能。它的目的是让您控制整个网络和所有设备，并且不需要使用客户端程序。

AdGuard Home 提供了一个美观、易用且功能丰富的 web 界面，可以轻松管理过滤过程及其设置。

## 安装

这个附加组件的安装非常简单，与安装其他 Home Assistant 附加组件并无不同。

1. **确保您的 Home Assistant 设备具有
   [静态 IP 和静态外部 DNS 服务器！](https://github.com/home-assistant/operating-system/blob/dev/Documentation/network.md#static-ip)**
   这很重要！如果您跳过此步骤，您 **将会** 遇到问题。
   - 在网络中更改此设置：
     [![打开您的 Home Assistant 实例并管理系统的网络配置。](https://my.home-assistant.io/badges/network.svg)](https://my.home-assistant.io/redirect/network/)
     (_设置 → 系统 → 网络
     → 配置网络接口 → 您的接口 → IPv4 → 静态_)
   - 请注意，在路由器中设置固定 IP **不是** 静态的。
1. 点击下面的 Home Assistant 我的按钮以在您的 Home Assistant 实例中打开该附加组件。

   [![在您的 Home Assistant 实例中打开此附加组件。][addon-badge]][addon]

1. 点击“安装”按钮以安装附加组件。
1. 启动“AdGuard Home”附加组件。
1. 检查“AdGuard Home”的日志，查看一切是否顺利进行。
1. 点击“打开 Web UI”按钮，使用您的 Home Assistant 帐户登录。
1. 准备就绪！

## 配置

**注意**：_更改配置时，请记得重新启动附加组件。_

附加组件配置示例：

```yaml
log_level: info
ssl: true
certfile: fullchain.pem
keyfile: privkey.pem
```

**注意**：_这只是一个示例，请不要直接复制粘贴！请创建您自己的！_

### 选项: `log_level`

`log_level` 选项控制附加组件的日志输出级别，可以更改为更详细或更少详细，这在处理未知问题时可能会很有用。可选值为：

- `trace`: 显示每个细节，类似于所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不是错误的异常情况。
- `error`: 不需要立即处理的运行时错误。
- `fatal`: 出现严重错误。附加组件变得不可用。

请注意，每个级别自动包括来自更高严重性级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您正在进行故障排除。

### 选项: `ssl`

启用/禁用附加组件的 SSL (HTTPS)。将其设置为 `true` 以启用，反之则设置为 `false`。

**注意**：_SSL 设置仅适用于直接访问，对 Ingress 服务没有影响。_

### 选项: `certfile`

用于 SSL 的证书文件。

**注意**：_文件必须存储在 `/ssl/` 中，这是默认位置_

### 选项: `keyfile`

用于 SSL 的私钥文件。

**注意**：_文件必须存储在 `/ssl/` 中，这是默认位置_

### 选项: `leave_front_door_open`

将此选项添加到附加组件配置中，可以通过将其设置为 `true` 来禁用 AdGuard Home 的身份验证。

**注意**：_我们强烈建议不使用此选项，即使该附加组件仅暴露在您的内部网络中。风险自负！_

## 加密设置（高级用法）

Adguard 允许本地配置运行 DNS-over-HTTPS 和 DNS-over-TLS。如果配置这些选项，请确保在此之后重启附加组件。此外，为了正确使用 DNS-over-HTTPS，请确保在附加组件和 Adguard 本身中也配置 SSL。同时请考虑附加组件和 Adguard 不能使用相同的端口进行 SSL。

## 更新日志与发布

此仓库使用 [GitHub 的发布][releases] 功能来维护变更日志。

发布基于 [语义化版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容递增：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题？

您有几种方式可以获得解答：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord]，用于附加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha]，用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 分论坛][reddit]。

您还可以在 [GitHub 上开一个问题][issue]。

## 作者与贡献者

本仓库的初始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2019-2025 Franck Nijhof

特此免费授权任何获得本软件及相关文档文件（“软件”）副本的人，不受限制地处理该软件，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或出售该软件的副本，并允许向其提供该软件的人照此做，但须遵守以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

本软件是“按原样”提供的，没有任何种类的保证，无论是明示或暗示，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对因使用本软件或其他交易而引起的任何索赔、损害或其他责任承担责任，无论是在合同、侵权或其他情况下。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_adguard&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[adguard]: https://adguard.com/adguard-home/overview.html
[contributors]: https://github.com/hassio-addons/addon-adguard-home/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-adguard-home/90684?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-adguard-home/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-adguard-home/releases
[semver]: https://semver.org/spec/v2.0.0.html