# Home Assistant 社区插件: AppDaemon

[AppDaemon][appdaemon] 是一个松耦合的多线程沙盒化 Python 执行环境，用于为 Home Assistant 家庭自动化软件编写自动化应用程序。它还提供一个可配置的仪表板 (HADashboard)，适合墙挂式平板电脑使用。

## 安装

该插件的安装非常简单，与安装其他 Home Assistant 插件没有区别。

1. 单击下面的 Home Assistant 我的按钮，以在您的 Home Assistant 实例中打开该插件。

   [![在您的 Home Assistant 实例中打开该插件。][addon-badge]][addon]

1. 单击“安装”按钮安装该插件。
1. 启动“AppDaemon”插件。
1. 检查“AppDaemon”插件的日志，以查看一切是否顺利。

:information_source: 请注意，该插件已预配置为连接 Home Assistant。无需在 AppDaemon 配置中创建访问令牌或设置您的 Home Assistant URL。

这种对 URL 和令牌的自动处理与 [AppDaemon 官方文档][appdaemon] 冲突。官方文档将指出需要 `ha_url` 和 `token` 选项。然而，对于这个插件，实际上不需要这些。

## 配置

**注意**: _修改配置后，请记得重启插件。_

示例插件配置：

```yaml
log_level: info
system_packages:
  - ffmpeg
python_packages:
  - PyMySQL
  - Pillow
```

**注意**: _这只是一个示例，请不要复制粘贴！请创建您自己的！_

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以根据需要调整详细程度，这在处理未知问题时可能很有帮助。可能的值有：

- `trace`: 显示每一个细节，比如所有被调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不属于错误的特殊情况。
- `error`: 运行时错误，不需要立即处理。
- `fatal`: 某些事情发生了严重错误。插件变得不可用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug` 还会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您正在进行故障排除。

这些日志级别也会影响 AppDaemon 的日志级别。

### 选项: `system_packages`

允许您指定要安装到 AppDaemon 设置中的其他 [Alpine 包][alpine-packages]（例如，`g++`、`make`、`ffmpeg`）。

**注意**: _添加许多包会导致插件启动时间更长。_

### 选项: `python_packages`

允许您指定要安装到 AppDaemon 设置中的其他 [Python 包][python-packages]（例如，`PyMySQL`、`Requests`、`Pillow`）。

**注意**: _添加许多包会导致插件启动时间更长。_

#### 选项: `init_commands`

使用 `init_commands` 选项进一步自定义您的环境。将一个或多个 shell 命令添加到列表中，每次该插件启动时都会执行这些命令。

## AppDaemon 和 HADashboard 配置

该插件不会为您配置 AppDaemon 或 HADashboard。它会创建一些示例文件，以便您在首次运行时开始进行配置。

AppDaemon 的配置可以在该插件的配置文件夹中找到。

有关配置 AppDaemon 的更多信息，请参考他们提供的详细文档：

<http://appdaemon.readthedocs.io/en/latest/>

## Home Assistant 访问令牌和 ha_url 设置

默认情况下，该插件未在 `appdaemon.yaml` 配置文件中自带 `token` 和 `ha_url`。**这不是错误！**

该插件为您处理这些设置，您无需在 AppDaemon 配置中提供或设置这些。

这种对 URL 和令牌的自动处理与 AppDaemon 官方文档冲突。官方文档将指出需要 `ha_url` 和 `token` 选项。然而，对于该插件，这些并不需要。

不过，如果您想覆盖它们，您可以自由设置，但在一般使用中，这通常不需要，并且不推荐对于该插件。

## 更新日志与发布

该存储库使用 [GitHub 的发布][releases] 功能保留变更日志。

版本基于 [语义版本控制][semver]，采用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下情况进行递增：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几种方式可以获得答案：

- [Home Assistant 社区插件 Discord 聊天服务器][discord] 提供插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 进行一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子论坛][reddit]。

您也可以在这里 [提出问题][issue] GitHub。

## 作者与贡献者

该存储库的初始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可

版权所有 (c) 2021 - 2025 Franck Nijhof

特此免费授予任何获得本软件及其相关文档文件（“软件”）副本的人，使用软件的权限，包括但不限于使用、复制、修改、合并、出版、分发、再授权和 / 或销售软件的副本，并允许向其提供软件的人这样做，条件如下：

上述版权声明和本许可声明应包括在软件的所有副本或实质部分中。

该软件按“原样”提供，不提供任何形式的担保，无论明示或暗示，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有人对任何索赔、损害或其他责任不承担责任，无论是在合同诉讼、侵权或其他方面，均因软件或其使用或其他交易而产生。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_appdaemon&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[alpine-packages]: https://pkgs.alpinelinux.org/packages
[appdaemon]: https://appdaemon.readthedocs.io
[contributors]: https://github.com/hassio-addons/addon-appdaemon/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-appdaemon-4/163259?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-appdaemon/issues
[python-packages]: https://pypi.org/
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-appdaemon/releases
[semver]: http://semver.org/spec/v2.0.0.htm