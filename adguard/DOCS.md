# Home Assistant Community Add-on: AdGuard Home

[AdGuard Home][adguard] 是一个网络范围内的广告和追踪器阻止DNS服务器，具有家长控制（成人内容阻止）功能。其目的是让您控制整个网络和所有设备，并且不需要使用客户端程序。

AdGuard Home 提供了一个美丽、易用且功能丰富的Web界面，以便轻松管理过滤过程及其设置。

## 安装

此插件的安装非常简单，和安装其他任何Home Assistant插件没有什么不同。

1. **确保您的Home Assistant设备具有
   [静态IP和静态外部DNS服务器！](https://github.com/home-assistant/operating-system/blob/dev/Documentation/network.md#static-ip)**
   这非常重要！如果您跳过此步骤，您**将**遇到问题。
   - 在网络中更改此设置：
     [![打开您的Home Assistant实例并管理您的系统网络配置。](https://my.home-assistant.io/badges/network.svg)](https://my.home-assistant.io/redirect/network/)
     （_设置 → 系统 → 网络 → 配置网络接口 → 您的接口 → IPv4 → 静态_）
   - 请注意，在路由器中设置固定IP**不是**静态的。
2. 点击下面的 Home Assistant My 按钮以在您的 Home Assistant 实例中打开插件。

   [![在您的Home Assistant实例中打开此插件。][addon-badge]][addon]

3. 点击“安装”按钮以安装插件。
4. 启动“AdGuard Home”插件。
5. 检查“AdGuard Home”的日志以查看一切是否顺利。
6. 点击“打开web UI”按钮，并使用您的Home Assistant帐户登录。
7. 准备好了！

## 配置

**注意**：_记得在配置更改时重启插件。_

示例插件配置：

```yaml
log_level: info
ssl: true
certfile: fullchain.pem
keyfile: privkey.pem
```

**注意**：_这只是一个示例，不要复制粘贴！创建您自己的！_

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能会有用。可选值为：

- `trace`: 显示每个细节，如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不属于错误的例外事件。
- `error`: 不需要立即处理的运行时错误。
- `fatal`: 发生严重错误。插件变得不可用。

请注意，每个级别会自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在故障排除。

### 选项: `ssl`

启用/禁用插件上的SSL（HTTPS）。设置为 `true` 以启用，设置为 `false` 则禁用。

**注意**：_SSL 设置仅适用于直接访问，对 Ingress 服务没有影响。_

### 选项: `certfile`

用于SSL的证书文件。

**注意**：_该文件必须存储在 `/ssl/` 中，这是默认位置_

### 选项: `keyfile`

用于SSL的私钥文件。

**注意**：_该文件必须存储在 `/ssl/` 中，这是默认位置_

### 选项: `leave_front_door_open`

将此选项添加到插件配置中可以通过将其设置为 `true` 来禁用 AdGuard Home 的身份验证。

**注意**：_我们强烈建议不要使用此选项，即使此插件只是暴露于您的内部网络中。请自负风险！_

## 加密设置（高级用法）

AdGuard 允许配置在本地运行 DNS-over-HTTPS 和 DNS-over-TLS。如果您配置这些选项，请确保在之后重启插件。此外，要正确使用 DNS-over-HTTPS，请确保在插件和 AdGuard 本身中都配置 SSL。还要考虑插件和 AdGuard 不能使用相同的端口进行 SSL。

## 更新日志和发布

此存储库使用 [GitHub 的发布][releases] 功能维护变更日志。

发布基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下内容递增：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几个选项来获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以 [在这里打开一个问题][issue] GitHub。

## 作者与贡献者

此存储库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

Copyright (c) 2019-2025 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人，在不受限制的情况下处理软件，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或销售软件副本的权利，并允许被提供软件的人这样做，前提是遵守以下条件：

上述版权声明和本许可证声明应包括在所有软件的副本或重要部分中。

本软件按“原样”提供，不提供任何种类的保证，无论是明示还是暗示，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对任何索赔、损害或其他责任负责，无论是在合同、侵权或其他方式中提出的，均因使用软件或其他交易而产生。

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