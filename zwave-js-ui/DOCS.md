# Home Assistant Community Add-on: Z-Wave JS UI

Z-Wave JS UI 插件提供了一个额外的控制面板，允许您配置 Z-Wave 网络的每个方面。它提供了一个解耦的网关，可以使用 Z-Wave JS WebSockets（用于 Home Assistant Z-Wave JS 集成）和 MQTT（甚至可以同时使用）进行通信。

一些优点和使用案例：

- 兼容 Home Assistant Z-Wave JS 集成。
- 您的 Z-Wave 网络将在 Home Assistant 重启之间继续运行。
- 您可以直接使用 Node-RED 等与您的 Z-Wave 网络进行交互，同时它也可以为 Home Assistant 提供服务。
- 允许基于 [ESPHome.io][esphome] 的 ESP 设备直接响应或与您的 Z-Wave 网络工作。
- 如果找到 Mosquitto 插件，会自动进行预配置。

此插件使用 [Z-Wave JS UI][zwave-js-ui] 软件。

## 安装

此插件的安装相对简单，与安装任何其他 Home Assistant 插件没有区别。

1. 点击下面的 Home Assistant 按钮，以在您的 Home Assistant 实例中打开插件。

   [![在您的 Home Assistant 实例中打开此插件。][addon-badge]][addon]

1. 点击“安装”按钮以安装插件。
1. 检查“Z-Wave JS UI”插件的日志以查看是否一切正常。
1. 点击“打开 Web UI”按钮。
1. 享受该插件！

**注意**：上游项目有关于使用该软件本身的文档：
<https://zwave-js.github.io/zwave-js-ui/#/>

## 设置 Home Assistant Z-Wave JS 集成

默认情况下，Home Assistant Z-Wave JS 集成将尝试从官方插件商店设置官方“Z-Wave JS”插件。

但是，此插件将提供一个插件 UI，并具有通过 MQTT 发送/接收数据的能力。因此，如果这是您所需要的，这个插件可能适合您。

成功启动插件后，是时候将其连接到 Home Assistant 了。

为此：

1. 点击监督者中的插件页面上的“打开 Web UI”按钮，打开 Z-Wave JS UI 控制面板。
1. 在控制面板中，转到菜单中的“设置”，然后点击右侧显示的“Zwave”栏。
1. 输入以下信息：
   - 串行端口（例如，`/dev/serial/by-id/usb-0658_0200_if00`）
   - 网络密钥（例如，`2232666D100F795E5BB17F0A1BB7A146`）

现在点击“保存”按钮并导航到菜单中的“控制面板”。
如果您已经与设备配对，您应该会看到它们逐渐显示出来。

现在是时候设置 Home Assistant 了：

1. 转到设置面板并点击“设备与服务”。
1. 在右下角，点击“+ 添加集成”。
1. 从列表中选择“Z-Wave”集成。
1. 将会显示一个对话框，询问您是否使用该插件：
   - **取消选中**该框，它将安装官方插件。
   - 再次强调，推荐使用官方插件，因此...
1. 在下一个对话框中，会询问服务器。输入：
   `ws://a0d7b954-zwavejs2mqtt:3000`
1. 确认，即可完成！

## 配置

**注意**：_记得在配置更改后重启插件。_

示例插件配置：

```yaml
log_level: info
```

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简略，这在处理未知问题时可能会很有用。可能值包括：

- `trace`: 显示每一个细节，例如所有被调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不是错误的异常情况。
- `error`: 不需要立即处理的运行时错误。
- `fatal`: 发生了严重错误。插件变得不可用。

请注意，每个级别自动包括来自更严厉级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐设置，除非您在故障排除。

## 已知问题与限制

- Z-Wave JS UI 支持通过 MQTT 进行 Home Assistant 发现。**强烈建议不使用**该选项。请使用上述文档中说明的 Z-Wave JS 集成。

## 更新日志与发布

该仓库使用 [GitHub 的发布][releases] 功能维护更改日志。

发布基于 [语义版本控制][semver]，格式为 `MAJOR.MINOR.PATCH`。简单来说，版本将根据以下内容进行增量更新：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

您有多种选择来得到解答：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord]，用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha]，用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子版块][reddit]。

您还可以在这里 [打开一个问题][issue] GitHub。

## 作者与贡献者

该仓库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2021 - 2025 Franck Nijhof

特此授予任何获得此软件及相关文档文件（“软件”）副本的人免费、无条件使用软件的权利，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售软件副本的权利，并允许向其提供软件的人这样做，前提是满足以下条件：

上述版权声明和本许可声明应包含在所有副本或软件的实质部分中。

本软件按“原样”提供，不作任何种类的担保，明示或暗示，包括但不限于对适销性、特定用途适用性和不侵权的担保。在任何情况下，作者或版权持有者不对任何索赔、损害或其他责任负责，无论是在合同诉讼、侵权或其他方面，由于使用软件或与软件的使用或其他交易而引起。

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