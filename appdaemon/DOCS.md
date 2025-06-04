# Home Assistant社区插件: AppDaemon

[AppDaemon][appdaemon] 是一个松散耦合的多线程沙盒Python执行环境，用于为Home Assistant家居自动化软件编写自动化应用程序。它还提供了一个可配置的仪表板（HADashboard），适合墙上安装的平板电脑。

## 安装

安装这个插件非常简单，与安装其他Home Assistant插件没有区别。

1. 点击下面的Home Assistant我的按钮以在您的Home Assistant实例中打开该插件。

   [![在您的Home Assistant实例中打开此插件。][addon-badge]][addon]

2. 点击“安装”按钮以安装插件。
3. 启动“AppDaemon”插件
4. 检查“AppDaemon”插件的日志以查看一切是否顺利。

:information_source: 请注意，该插件已预先配置以连接Home Assistant。无需在AppDaemon配置中创建访问令牌或设置您的Home Assistant URL。

这种对URL和令牌的自动处理与[AppDaemon官方文档][appdaemon]相冲突。官方文档将说明`ha_url`和`token`选项是必需的。然而，对于该插件，这并不需要。

## 配置

**注意**: _更改配置时请记得重启插件。_

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

`log_level`选项控制插件的日志输出级别，可以更改为更加或更少详细，这在您处理未知问题时可能会有用。可能的值有：

- `trace`: 显示每个细节，比如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不属于错误的特殊情况。
- `error`: 运行时错误，不要求立即采取行动。
- `fatal`: 出现了严重错误。插件变得不可用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug`也会显示`info`消息。默认情况下，`log_level`被设置为`info`，这是推荐的设置，除非您在故障排除。

这些日志级别也影响AppDaemon的日志级别。

### 选项: `system_packages`

允许您指定要安装到AppDaemon设置中的其他[Alpine包][alpine-packages]（例如，`g++`、`make`、`ffmpeg`）。

**注意**: _添加许多包将导致插件启动时间更长。_

### 选项: `python_packages`

允许您指定要安装到AppDaemon设置中的其他[Python包][python-packages]（例如，`PyMySQL`、`Requests`、`Pillow`）。

**注意**: _添加许多包将导致插件启动时间更长。_

#### 选项: `init_commands`

使用`init_commands`选项进一步自定义您的环境。将一个或多个shell命令添加到列表中，它们将在每次启动此插件时执行。

## AppDaemon和HADashboard配置

此插件不会为您配置AppDaemon或HADashboard。它确实会创建一些示例文件，帮助您在第一次运行时入门。

AppDaemon的配置可以在此插件的插件配置文件夹中找到。

有关配置AppDaemon的更多信息，请参考他们提供的详细文档：

<http://appdaemon.readthedocs.io/en/latest/>

## Home Assistant访问令牌和ha_url设置

默认情况下，此插件不带`token`和在`appdaemon.yaml`配置文件中没有`ha_url`。 **这不是错误！**

插件为您处理这些设置，您不需要在AppDaemon配置中提供或设置这些。

这种对URL和令牌的自动处理与AppDaemon官方文档相冲突。官方文档将说明`ha_url`和`token`选项是必需的。对于该插件，这些并不需要。

不过，如果您想要覆盖它们，您可以自由设置，但通常情况下，不需要这样做，并且不建议为此插件这样做。

## 更新日志与发布

该仓库使用[GitHub的发布][releases]功能保留变更日志。

发布基于[语义化版本控制][semver]，并使用格式`MAJOR.MINOR.PATCH`。简而言之，版本将基于以下内容递增：

- `MAJOR`: 不兼容或重大改变。
- `MINOR`: 向后兼容的新特性和增强。
- `PATCH`: 向后兼容的BUG修复和包更新。

## 支持

有问题吗？

您有几种选择来获取答案：

- [Home Assistant社区插件Discord聊天服务器][discord]以获取插件支持和功能请求。
- [Home Assistant Discord聊天服务器][discord-ha]以获取一般Home Assistant讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入[Reddit subreddit][reddit]中的[/r/homeassistant][reddit]。

您还可以在这里[打开一个问题][issue] GitHub。

## 作者与贡献者

该仓库的最初设置由[Franck Nijhof][frenck]完成。

有关所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权所有 (c) 2021 - 2025 Franck Nijhof

特此授予任何获得本软件及相关文档文件（"软件"）副本的人，免费使用本软件的权利，包括不限于使用、复制、修改、合并、出版、分发、再授权和/或销售本软件副本的权利，以及允许向其提供软件的人这样做，但必须遵循以下条件：

上述版权声明和本许可声明应包含在所有副本或软件的实质性部分中。

本软件是按"原样"提供，不提供任何类型的担保，无论是明示还是暗示，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有人对任何索赔、损害或其他责任均不承担责任，无论是在合同诉讼、侵权诉讼或其他方面，因本软件或其使用或其他交易而产生。

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