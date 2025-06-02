# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理 UI，允许您轻松管理 Docker 主机或 Docker 群集。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件功能强大，可让您几乎访问整个系统。虽然该插件是以安全为前提小心创建和维护的，但在错误或缺乏经验的用户手中，它可能会损坏您的系统。

## 警告 2

Portainer 插件旨在调试 Home Assistant 及其容器。它并不用于管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器**。忽视这一点将使您的系统变为不受支持！

## 安装

要安装此插件，您首先需要到您的个人资料中打开“高级模式”，完成后返回 Home Assistant 插件并搜索“Portainer”，然后像安装其他插件一样安装它。

要能够使用此插件，您需要在该插件上禁用保护模式。没有它，插件将无法访问 Docker。

1. 在管理器插件商店中搜索“Portainer”插件并安装。
2. 将“保护模式”开关设置为关闭。
3. 启动“Portainer”插件。
4. 检查“Portainer”插件的日志，以查看一切是否顺利。

## 配置

**注意**: _记得在更改配置时重新启动插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**: _这只是一个示例，不要直接复制粘贴！创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简略，这在处理未知问题时可能会很有用。可能的值包括：

- `trace`：显示每个细节，如所有调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）感兴趣的事件。
- `warning`：不是错误的例外事件。
- `error`：不需要立即处理的运行时错误。
- `fatal`：发生了严重错误。插件变得无法使用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug` 还会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您正在排查问题。

### 选项：`agent_secret`

设置共享代理秘密的选项。必须在远程代理中作为环境变量设置。

## 变更日志与发布

该存储库使用 [GitHub 的发布][releases] 功能维护变更日志。

发布基于 [语义化版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下情况进行增量更新：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

您有几种方式可以获得解答：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord]，用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha]，用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 论坛][reddit]，在 [/r/homeassistant][reddit] 中。

您也可以在这里 [提交问题][issue] 到 GitHub。

## 作者与贡献者

该存储库的原始设置由 [Franck Nijhof][frenck] 完成。

要查看全部作者和贡献者的名单，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此免费授权获得本软件及相关文档文件（“软件”）的任何人，在不受限制的情况下处理该软件，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或出售该软件的副本，并允许提供软件的人这样做，符合以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件是按“原样”提供的，不提供任何形式的担保，无论明示或暗示，包括但不限于适销性、特定用途的适用性和不侵权的担保。在任何情况下，作者或版权持有人对因使用软件或与软件使用或其他交易相关的合同、侵权或其他性质的任何索赔、损害或其他责任不承担责任。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm