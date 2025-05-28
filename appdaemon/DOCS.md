# Home Assistant社区插件：AppDaemon

[AppDaemon][appdaemon] 是一个松耦合的、多线程的、沙盒化的Python执行环境，用于编写Home Assistant家庭自动化软件的自动化应用。它还提供了一个可配置的仪表板（HADashboard），适合墙上安装的平板电脑。

## 安装

这个插件的安装非常简单，和安装任何其他Home Assistant插件没有什么不同。

1. 点击下面的Home Assistant按钮，以在您的Home Assistant实例中打开插件。

   [![在您的Home Assistant实例中打开此插件。][addon-badge]][addon]

2. 点击“安装”按钮，安装该插件。
3. 启动“AppDaemon”插件。
4. 检查“AppDaemon”插件的日志，看看一切是否正常。

:information_source: 请注意，该插件已预配置为连接Home Assistant。无需在AppDaemon配置中创建访问令牌或设置您的Home Assistant URL。

这种自动处理URL和令牌的方式与[AppDaemon官方文档][appdaemon]相冲突。官方文档中会指出`ha_url`和`token`选项是必需的。然而，对于此插件，这些不是必需的。

## 配置

**注意**：_当配置发生更改时，请记得重启插件。_

示例插件配置：

```yaml
log_level: info
system_packages:
  - ffmpeg
python_packages:
  - PyMySQL
  - Pillow
```

**注意**：_这只是一个示例，请不要复制粘贴！自己创建一个！_

### 选项：`log_level`

`log_level`选项控制插件输出的日志级别，可以更改为更详细或更简洁，这在处理未知问题时可能会很有用。可以的值有：

- `trace`: 显示每个细节，如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不是错误的异常情况。
- `error`: 在运行时发生的错误，不需要立即采取行动。
- `fatal`: 出现了严重问题。插件变得不可用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug`也会显示`info`消息。默认情况下，`log_level`设置为`info`，这是推荐的设置，除非您在排错。

这些日志级别也会影响AppDaemon的日志级别。

### 选项：`system_packages`

允许您指定要安装到AppDaemon设置中的其他[Alpine软件包][alpine-packages]（例如，`g++`、`make`、`ffmpeg`）。

**注意**：_添加许多软件包将导致插件的启动时间变长。_

### 选项：`python_packages`

允许您指定要安装到AppDaemon设置中的其他[Python软件包][python-packages]（例如，`PyMySQL`、`Requests`、`Pillow`）。

**注意**：_添加许多软件包将导致插件的启动时间变长。_

#### 选项：`init_commands`

使用`init_commands`选项进一步自定义您的环境。将一个或多个shell命令添加到列表中，它们将在每次该插件启动时执行。

## AppDaemon和HADashboard配置

此插件不会为您配置AppDaemon或HADashboard。不过，它确实会创建一些示例文件，以帮助您在第一次运行时入门。

AppDaemon的配置可以在此插件的配置文件夹中找到。

有关配置AppDaemon的更多信息，请参考他们提供的详细文档：

<http://appdaemon.readthedocs.io/en/latest/>

## Home Assistant访问令牌和ha_url设置

默认情况下，此插件不包含`token`，在`appdaemon.yaml`配置文件中没有`ha_url`。 **这不是错误！**

此插件为您处理这些设置，您无需在AppDaemon配置中提供或设置这些。

这种自动处理URL和令牌的方式与AppDaemon官方文档相冲突。官方文档中会指出`ha_url`和`token`选项是必需的。然而，对于此插件，这些不是必需的。

但是，如果您想要覆盖它们，可以自己设置，通常情况下，这并不需要，也不推荐在此插件中这样做。

## 更新日志和发布

该存储库使用[GitHub的版本][releases]功能保持变更日志。

发布是基于[语义版本控制][semver]，使用`MAJOR.MINOR.PATCH`格式。简而言之，版本将根据以下条件增加：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

您有多种选择可以获取答案：

- [Home Assistant Community Add-ons Discord聊天服务器][discord]以获得插件支持和功能请求。
- [Home Assistant Discord聊天服务器][discord-ha]以进行一般的Home Assistant讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入Reddit上的[subreddit][reddit]中的 [/r/homeassistant][reddit]

您也可以在这里[打开一个问题][issue] GitHub。

## 作者和贡献者

此存储库的最初设置由[Franck Nijhof][frenck]完成。

有关所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权所有 (c) 2021 - 2025 Franck Nijhof

特此授予免费获得本软件及相关文档文件（“软件”的任何人一份副本）使用此软件而不受限制的权限，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或出售该软件的副本，并允许提供该软件的人这样做，遵循以下条件：

上述版权声明和本许可声明应包含在所有副本或软件的重大部分中。

本软件是在“现状”下提供的，不附有任何种类的保证，无论是明示或暗示，包括但不限于适销性、特定用途的适用性和不侵权。在任何情况下，作者或版权持有人均不对因使用本软件或与本软件的使用或其他交易有关的任何索赔、损害或其他责任承担任何责任，无论是在合同诉讼、侵权或其他方面。

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