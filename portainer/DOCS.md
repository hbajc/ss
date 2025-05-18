# Home Assistant Community Add-on: Portainer

Portainer 是一个开源轻量级管理界面，允许您轻松管理一个或多个 Docker 主机或 Docker swarm 集群。

管理 Docker 从未如此简单。Portainer 提供了详细的 Docker 概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件非常强大，几乎可以访问您整个系统。虽然这个插件是经过小心创建和维护的，并且考虑到了安全性，但在不当或缺乏经验的操作下，可能会损坏您的系统。

## 警告 2

Portainer 插件旨在调试 Home Assistant 及其容器。它并非设计用来管理或部署您自定义的软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器。** 忽视这一点会使您的系统被视为不支持的状态！

## 安装

要安装此插件，首先需要进入您的个人资料并启用 “高级模式”。完成后，返回 Home Assistant 插件页面，搜索“Portainer”并像安装其他插件一样进行安装。

要能够使用此插件，您需要禁用此插件的保护模式。没有它，插件将无法访问 Docker。

1. 在 Supervisor 插件商店中搜索 “Portainer” 插件并安装它。
1. 将 “保护模式” 开关设置为关闭。
1. 启动 “Portainer” 插件。
1. 检查 “Portainer” 插件的日志，查看是否一切正常。

## 配置

**注意**: _记得在更改配置后重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**: _这只是一个示例，请不要直接复制粘贴！请创建您自己的配置！_

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简单，这在处理未知问题时可能会很有用。可能的值有：

- `trace`: 显示每一个细节，比如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不是错误的例外情况。
- `error`: 不需要立即采取行动的运行时错误。
- `fatal`: 出现严重问题。插件变得不可用。

请注意，每个级别自动包含来自更严重级别的日志消息，例如，`debug` 还会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在排查故障。

### 选项: `agent_secret`

一个选项，用于设置共享代理秘密。必须在远程代理中也作为环境变量进行设置。

## 更新日志与版本发布

该存储库使用 [GitHub 的发布][releases] 功能保持变更日志。

发布基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本会根据以下内容增加：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强功能。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题？

您有几种方式可以获得回答：

- Home Assistant 社区插件 Discord 聊天服务器 [Discord][discord]，提供插件支持和功能请求。
- Home Assistant Discord 聊天服务器 [Discord][discord-ha]，进行 Home Assistant 的一般讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子论坛][reddit] 在 [/r/homeassistant][reddit]。

您还可以 [在这里提出问题][issue] GitHub。

## 作者与贡献者

该存储库的原始设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2018-2021 Franck Nijhof

特此授予任何获得本软件及相关文档文件（“软件”）副本的人，无限制地处理该软件，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许向其提供软件的人员这样做，条件如下：

上述版权声明和本许可声明应包含在所有软件副本或实质性部分中。

软件是按“原样”提供的，不提供任何明示或暗示的担保，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有者都不对因使用软件或其他交易而产生的任何索赔、损害或其他责任承担责任，无论是在合同、侵权或其他方面。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm