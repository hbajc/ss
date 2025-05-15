# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理用户界面，它可以让您轻松管理 Docker 主机或 Docker 群集。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概览，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件非常强大，可以访问您几乎整个系统。尽管这个插件是经过仔细创建和维护，并考虑到安全性，在错误或缺乏经验的手中，它可能会损害您的系统。

## 警告 2

Portainer 插件旨在调试 Home Assistant 及其容器。它并不是为了管理或部署您的自定义软件或第三方容器而设计的。

**Home Assistant 不支持在 Home Assistant OS 或被监督安装类型上运行第三方容器**。忽视这一点会使您的系统变得不受支持！

## 安装

要安装此插件，您需要首先去您的个人资料并打开“高级模式”，完成后返回 Home Assistant 插件，并搜索“Portainer”并像安装其他插件一样进行安装。

要能够使用此插件，您需要禁用此插件上的保护模式。没有它，该插件无法访问 Docker。

1. 在 Supervisor 插件商店中搜索“Portainer”插件并安装它。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”插件。
1. 检查“Portainer”插件的日志，以查看一切是否顺利。

## 配置

**注意**：_记得在配置更改时重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，请不要复制粘贴！创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁的输出，这在处理未知问题时可能会很有用。可能的值有：

- `trace`: 显示每一个细节，例如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 普通（通常）有趣的事件。
- `warning`: 不是错误的特殊情况。
- `error`: 不需要立即采取行动的运行时错误。
- `fatal`: 发生了严重错误，插件变得不可用。

请注意，每个级别会自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在进行故障排除。

### 选项：`agent_secret`

设置共享代理密钥的选项。必须在远程代理中也作为环境变量进行设置。

## 更新日志和版本

该存储库使用 [GitHub 的发布功能][releases] 保持变更日志。

版本基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下内容进行增加：

- `MAJOR`: 不兼容或重大变化。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修正和软件包更新。

## 支持

有问题吗？

您有几种选择可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子版块][reddit]。

您也可以 [在这里打开问题][issue] GitHub。

## 作者和贡献者

此存储库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此授予任何获取本软件及相关文档文件（“软件”）副本的人，无偿处理软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或出售软件副本的权利，并允许向其提供软件的人这样做，遵循以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不作任何形式的明示或暗示保证，包括但不限于对适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对因使用或其他交易与软件有关的任何索赔、损害或其他责任负责，无论是在合同诉讼、侵权或其他情况下。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm