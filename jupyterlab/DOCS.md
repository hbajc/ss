# Home Assistant Community Add-on: JupyterLab

JupyterLab 是一个开源的 Web 应用程序，允许您创建和分享包含实时代码、方程式、可视化和叙述文本的文档。用途包括：数据清理和转化、数值模拟、统计建模、数据可视化、机器学习等。

该附加组件运行 JupyterLab，这是 Project Jupyter 的下一代用户接口。它是一个可扩展的交互式和可重现计算环境，基于 Jupyter Notebook 和架构。

## 安装

这个附加组件的安装非常简单，与安装其他 Home Assistant 附加组件没有区别。

1. 点击下面的 Home Assistant 我的按钮以在您的 Home Assistant 实例中打开该附加组件。

   [![在你的 Home Assistant 实例中打开这个附加组件。][addon-badge]][addon]

1. 点击“安装”按钮以安装附加组件。
1. 启动“JupyterLab”附加组件。
1. 检查“JupyterLab”附加组件的日志以查看一切是否顺利。

## 配置

**注意**：_请记住，在更改配置时重新启动附加组件。_

示例附加组件配置：

```yaml
log_level: info
github_access_token: abcdef1234567890abcdef0123456789abcdef01
system_packages:
  - ffmpeg
init_commands:
  - pip install virtualenv
  - pip install yamllint
```

**注意**：_这只是一个示例，请不要复制和粘贴！请创建您自己的配置！_

### 选项：`log_level`

`log_level` 选项控制附加组件的日志输出级别，可以更改为更详细或更少详细，这在处理未知问题时可能会很有用。可能的值包括：

- `trace`：显示每个细节，例如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常情况但不是错误。
- `error`：运行时错误，但不需要立即处理。
- `fatal`：出现严重错误，附加组件变得不可用。

请注意，每个级别自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在进行故障排除。

### 选项：`github_access_token`

设置 GitHub 访问令牌。当对 GitHub 进行未认证请求时（因为我们必须这样做以获取仓库数据），GitHub 对我们可以发起的请求数量施加了相当严格的速率限制。因此，在几分钟的工作时间内，您可能会达到该限制。

文档中有一章说明获取此类令牌的步骤。

**注意**：_此选项支持机密，例如 `!secret github_token`。_

### 选项：`system_packages`

允许您指定要安装到 JupyterLab 设置中的附加 [Debian 包][debian-packages]（例如，`g++`、`make`、`ffmpeg`）。

**注意**：_添加许多包将导致附加组件的启动时间变 longer。_

#### 选项：`init_commands`

使用 `init_commands` 选项进一步自定义您的环境。将一个或多个 shell 命令添加到列表中，它们将在每次启动此附加组件时执行。

## 获取 GitHub 访问令牌

您可以按照以下步骤获取访问令牌：

1. [验证][github-verify]您的电子邮件地址与 GitHub。
1. 转到您在 GitHub 的帐户设置，然后从左侧面板选择“开发者设置”。
1. 在左侧，选择“个人访问令牌”。
1. 点击“生成新令牌”按钮，并输入您的密码。
1. 给令牌一个描述，并勾选“**repo**”作用域框。
1. 点击“生成令牌”。
1. 您应该得到一个字符串，这将是您的访问令牌。

请记住，这个令牌实际上是您 GitHub 帐户的密码。_请勿_ 在线共享或将令牌检入版本控制，因为其他人可以用它来访问您在 GitHub 上的所有数据。

## 更新日志与发布

此仓库使用 [GitHub 的发布][releases] 功能保持变更日志。

发布基于 [语义版本控制][semver]，并使用格式 `MAJOR.MINOR.PATCH`。简而言之，版本将根据以下内容进行增量：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新特性和增强。
- `PATCH`：向后兼容的bug修复和包更新。

## 支持

有问题？

您有几种方式可以获取答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 以获取附加组件的支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 以进行一般 Home Assistant 讨论和提问。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您还可以在这里 [提出问题][issue] GitHub。

## 作者与贡献者

此仓库的最初设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2025 Franck Nijhof

特此免费授权任何获得本软件及其相关文档文件（“软件”）副本的人，在软件内无任何限制地处理，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，以及允许提供软件的人这样做，遵循以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件是“按原样”提供的，不提供任何种类的担保，无论是明示或暗示，包括但不限于对适销性、特定目的适用性和非侵权的担保。在任何情况下，作者或版权持有人对任何索赔、损害或其他责任不承担责任，无论是在合同诉讼、侵权诉讼或其他任何情况下，因使用、与软件或其他交易相关的行为所产生。

[addon-badge]: https://my.home-assistant.io/badges/supervisor_addon.svg
[addon]: https://my.home-assistant.io/redirect/supervisor_addon/?addon=a0d7b954_jupyterlablite&repository_url=https%3A%2F%2Fgithub.com%2Fhassio-addons%2Frepository
[debian-packages]: https://www.debian.org/distrib/packages
[contributors]: https://github.com/hassio-addons/addon-jupyterlab/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-jupyterlab/87337?u=frenck
[frenck]: https://github.com/frenck
[github-verify]: https://help.github.com/articles/verifying-your-email-address
[issue]: https://github.com/hassio-addons/addon-jupyterlab/issues
[python-packages]: https://pypi.org/
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-jupyterlab/releases
[semver]: https://semver.org/spec/v2.0.0.html