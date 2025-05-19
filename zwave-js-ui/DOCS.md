# Home Assistant 社区附加组件: Z-Wave JS UI

Z-Wave JS UI 附加组件提供了一个额外的控制面板，允许您配置 Z-Wave 网络的每个方面。它提供了一个解耦的网关，可以通过 Z-Wave JS WebSockets（Home Assistant Z-Wave JS 集成使用）和 MQTT（甚至可以同时使用）进行通信。

一些优势和使用案例：

- 与 Home Assistant Z-Wave JS 集成兼容。
- 您的 Z-Wave 网络在 Home Assistant 重启之间将保持运行。
- 您可以直接使用 Node-RED 等设备与您的 Z-Wave 网络进行交互，同时它也可用于 Home Assistant。
- 允许基于 [ESPHome.io][esphome] 的 ESP 设备直接响应或与您的 Z-Wave 网络一起工作。
- 当找到 Mosquitto 附加组件时，它会自动进行预配置。

此附加组件使用 [Z-Wave JS UI][zwave-js-ui] 软件。

## 安装

安装此附加组件非常简单，与安装任何其他 Home Assistant 附加组件没有区别。

1. 点击下面的 Home Assistant 我的按钮，以在您的 Home Assistant 实例中打开该附加组件。

   [![在您的 Home Assistant 实例中打开此附加组件。][addon-badge]][addon]

1. 点击“安装”按钮以安装该附加组件。
1. 检查“Z-Wave JS UI”附加组件的日志以查看一切是否顺利进行。
1. 点击“打开Web UI”按钮。
1. 享受这个附加组件！

**注意**：上游项目有关于使用该软件本身的文档：
<https://zwave-js.github.io/zwave-js-ui/#/>

## 设置 Home Assistant Z-Wave JS 集成

默认情况下，Home Assistant Z-Wave JS 集成将尝试从官方附加组件商店设置官方“Z-Wave JS”附加组件。

然而，此附加组件将提供一个附加组件 UI，并具有通过 MQTT 发送/接收数据的能力。因此，如果您需要这个功能，这个附加组件可能适合您。

在成功启动附加组件后，您可以将其与 Home Assistant 连接。

为此：

1. 通过单击 Supervisor 页面上的“打开 Web UI”按钮打开 Z-Wave JS UI 控制面板。
1. 在控制面板中，转到菜单中的“设置”，然后点击右侧出现的“Zwave”栏。
1. 输入以下信息：
   - 串口 (例如，`/dev/serial/by-id/usb-0658_0200_if00`)
   - 网络密钥 (例如，`2232666D100F795E5BB17F0A1BB7A146`)

现在点击“保存”按钮，并在菜单中导航到“控制面板”。如果您已经配对了设备，它们应该会逐渐出现。

现在是设置 Home Assistant 的时候了：

1. 转到设置面板，点击“设备与服务”。
1. 在右下角，点击“+ 添加集成”。
1. 从列表中选择“Z-Wave”集成。
1. 将显示一个对话框，询问是否使用该附加组件：
   - **取消勾选**该选框，它将安装官方附加组件。
   - 同样，推荐使用官方附加组件，因此...
1. 在下一个对话框中将询问服务器。输入：
   `ws://a0d7b954-zwavejs2mqtt:3000`
1. 确认完成！

## 配置

**注意**: _记得在更改配置时重启附加组件。_

附加组件配置示例：

```yaml
log_level: info
```

### 选项: `log_level`

`log_level` 选项控制附加组件的日志输出级别，可以根据需要更改为更详细或更少详细，这在处理未知问题时可能会很有用。可能的值包括：

- `trace`：显示每个细节，如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：不属于错误的特殊情况。
- `error`：运行时错误，通常不需要立即处理。
- `fatal`：出现严重错误，附加组件变得不可用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这通常是推荐的设置，除非您正在进行故障排除。

## 已知问题和限制

- Z-Wave JS UI 支持通过 MQTT 进行 Home Assistant 发现。强烈建议**不要**使用该选项。请使用上面文档中提到的 Z-Wave JS 集成。

## 更新日志与发布

此存储库使用 [GitHub 的发布][releases] 功能保持更改日志。

发布基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将基于以下内容增加：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新特性和增强功能。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题？

您有多个选项可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于附加组件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您也可以在 [GitHub 上开个问题][issue]。

## 作者与贡献者

此存储库的原始设置由 [Franck Nijhof][frenck] 进行。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2021 - 2025 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人，允许在软件中进行不受限制的使用，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售软件的副本，并允许对其提供的软件的人这样做，须遵守以下条件：

上述版权声明和本许可声明应包含在所有副本或软件的实质性部分中。

本软件按“原样”提供，不含任何类型的保证，无论明示或暗示，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对因使用本软件或其他交易引起的任何索赔、损害或其他责任负责，无论是在合同诉讼、侵权或其他诉讼中。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_zwavejs2mqtt&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[contributors]: https://github.com/hassio-addons/addon-zwave-js-ui/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[esphome]: https://esphome.io/components/mqtt.html#on-message-trigger
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-zwave-js-ui/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-zwave-js-ui/releases
[semver]: https://semver.org/spec/v2.0.0.html
[zwave-js-ui]: https://github.com/zwave-js/zwave-js-ui