# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理用户界面，允许您轻松管理 Docker 主机或 Docker swarm 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件功能强大，可以访问您几乎整个系统。虽然这个插件是在小心和安全的考虑下创建和维护的，但在错误或缺乏经验的手中，可能会对您的系统造成损害。

## 警告 2

Portainer 插件用于调试 Home Assistant 及其容器。它并非旨在管理或部署您自定义的软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或受监督安装类型上运行第三方容器。** 忽视这一点将导致您的系统不受支持！

## 安装

要安装此插件，您首先需要转到您的配置文件并开启“高级模式”，完成后返回 Home Assistant 插件并搜索“Portainer”，然后像安装其他插件一样安装它。

要能够使用此插件，您需要在此插件上禁用保护模式。没有它，插件将无法访问 Docker。

1. 在管理者插件商店搜索“Portainer”插件并安装它。
1. 将“保护模式”开关设为关闭。
1. 启动“Portainer”插件。
1. 检查“Portainer”插件的日志，以确认一切正常。

## 配置

**注意**: _请记得在更改配置时重新启动插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**: _这只是一个示例，别复制粘贴！请创建您自己的！_

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以根据需要更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`: 显示每个细节，例如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 异常事件，但不是错误。
- `error`: 不需要立即采取的运行时错误。
- `fatal`: 发生了重大错误。插件变得不可用。

请注意，每个级别会自动包含更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在进行故障排除。

### 选项: `agent_secret`

一个设置共享代理秘密的选项。也必须在远程代理中作为环境变量设置。

## 更新日志与发布

此仓库使用 [GitHub 的发布][releases] 功能保持更改日志。

发布基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容进行增量更新：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几种方式可以获取答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 获取插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 进行一般 Home Assistant 讨论和提问。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子版块][reddit]。

您还可以在这里 [打开问题][issue] GitHub。

## 作者与贡献者

此仓库的最初设置由 [Franck Nijhof][frenck] 完成。

如需完整的所有作者和贡献者列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2018-2021 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（“软件”）副本的人，使用本软件而不受限制的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售该软件的副本的权利，以及允许本软件的受让人这样做，前提是遵守以下条件：

上述版权声明和本许可声明应包含在所有副本或实质性部分的软件中。

软件以“原样”提供，不提供任何形式的担保，无论是明示的还是暗示的，包括但不限于对适销性、适合特定目的和不侵权的担保。在任何情况下，作者或版权持有人不对因使用软件或其他交易中的软件而引起的任何索赔、损害或其他责任承担责任，无论是合同诉讼、侵权还是其他。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm