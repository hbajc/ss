# Home Assistant Community Add-on: Portainer

Portainer 是一款开源的轻量级管理用户界面，它使您能够轻松管理 Docker 主机或 Docker swarm 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件非常强大，几乎可以访问您整个系统。虽然这个插件是经过精心创建和维护，并考虑到安全性，但在错误或缺乏经验的使用者手中，它可能会损坏您的系统。

## 警告 2

Portainer 插件是为了调试 Home Assistant 及其容器而设计的。它并不旨在或设计为管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器**。忽视这一点，将使您的系统变为不受支持！

## 安装

要安装此插件，首先需要进入您的个人资料并开启“高级模式”，完成后返回到 Home Assistant 插件并搜索“Portainer”，然后像其他插件一样安装它。

要能够使用此插件，您需要禁用该插件的保护模式。没有它，插件无法访问 Docker。

1. 在 Supervisor 插件商店中搜索“Portainer”插件并安装它。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”插件。
1. 检查“Portainer”插件的日志以查看一切是否正常。

## 配置

**注意**: _在更改配置后请记得重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**: _这只是一个示例，请勿复制粘贴！创建您自己的！_

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以根据需要更改为更多或更少的详细信息，这在处理未知问题时可能会很有用。可能的值有：

- `trace`: 显示每一个细节，比如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不是错误的异常事件。
- `error`: 不需要立即采取行动的运行时错误。
- `fatal`: 某些事情出了严重问题。插件变得不可用。

请注意，每个级别自动包含来自更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您正在排除故障。

### 选项: `agent_secret`

一个选项，用于设置共享的代理密钥。必须在远程代理中作为环境变量进行设置。

## 变更日志与版本发布

本仓库使用 [GitHub 的版本发布][releases] 功能保持变更日志。

版本发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 格式。简而言之，版本将根据以下内容进行递增：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几个选项来获取答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 以获得插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 以进行一般的 Home Assistant 讨论和提问。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

您还可以在 [这里打开问题][issue] GitHub。

## 作者与贡献者

这个仓库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2018-2021 Franck Nijhof

特此授予任何获得本软件及相关文档文件（“软件”）副本的人免费、不受限制地处理本软件，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售本软件的副本的权利，以及允许向其提供该软件的人这样做，受以下条件的限制：

上述版权声明和本许可证声明应包含在所有本软件的副本或主要部分中。

软件以“原样”提供，不提供任何种类的明示或暗示的担保，包括但不限于对适销性、适合特定目的和不侵权的担保。在任何情况下，作者或版权持有人均不对因使用或其他与本软件有关的交易而引起的任何索赔、损害或其他责任负责，无论是在合同、侵权或其他方面。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm