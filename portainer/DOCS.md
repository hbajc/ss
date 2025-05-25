# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理 UI，允许您轻松管理 Docker 主机或 Docker swarm 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概览，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件功能强大，可以让您几乎访问整个系统。虽然这个插件是在考虑安全的前提下精心创建和维护的，但在错误或缺乏经验的手中，它可能会损坏您的系统。

## 警告 2

Portainer 插件旨在调试 Home Assistant 及其容器。它并不打算或设计用于管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器**。忽视这一点，会导致您的系统不被支持！

## 安装

要安装此插件，您首先需要去您的个人资料并开启“高级模式”，完成后返回 Home Assistant 插件并搜索 “Portainer”，像安装其他插件一样安装它。

要能够使用此插件，您需要禁用此插件上的保护模式。没有它，插件无法访问 Docker。

1. 在 Supervisor 插件商店中搜索 “Portainer” 插件并安装它。
1. 将“保护模式”开关设置为关闭。
1. 启动 “Portainer” 插件。
1. 检查 “Portainer” 插件的日志，查看是否一切正常。

## 配置

**注意**: _更改配置后记得重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**: _这只是一个示例，不要直接复制粘贴！创建您自己的！_

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能会很有用。可能的值如下：

- `trace`: 显示每个细节，例如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）感兴趣的事件。
- `warning`: 不是错误的异常情况。
- `error`: 运行时错误，不需要立即采取行动。
- `fatal`: 发生了严重错误；插件变得不可用。

请注意，每个级别自动包含来自更严重级别的日志消息，例如，`debug` 也显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在排除故障。

### 选项: `agent_secret`

设置共享代理秘密的选项。必须在远程代理中作为环境变量设置。

## 更新日志和发行版

此仓库使用 [GitHub 的发行版][releases] 功能保持变更日志。

发行版基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下内容递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和软件包更新。

## 支持

有问题吗？

您有几种方式可以得到答案：

- 用于插件支持和功能请求的 [Home Assistant Community Add-ons Discord 聊天服务器][discord]。
- 用于 Home Assistant 一般讨论和问题的 [Home Assistant Discord 聊天服务器][discord-ha]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

您还可以在这里 [提交问题][issue] 到 GitHub。

## 作者和贡献者

此仓库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此免费授予任何获得本软件及相关文档文件（以下简称“软件”）副本的人，对该软件进行无限制的使用权，包括使用、复制、修改、合并、发布、分发、再许可和/或销售该软件副本的权利，以及允许任何提供给该软件的人这样做，但须遵守以下条件：

上述版权声明和本许可声明应包括在所有副本或软件的实质性部分中。

该软件是按“原样”提供的，没有任何形式的明示或暗示的保证，包括但不限于对适销性、特定用途适用性和不侵权的保证。在任何情况下，作者或版权持有人均不对因使用该软件或与该软件或其他交易相关的任何索赔、损害或其他责任承担责任，无论是合同诉讼、侵权诉讼还是其他形式的诉讼。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm