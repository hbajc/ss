# Home Assistant Community Add-on: Portainer

Portainer 是一个开源轻量级管理 UI，可让您轻松管理 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件非常强大，使您几乎可以访问整个系统。尽管这个插件是经过仔细创建和维护的，并考虑了安全性，但在错误或缺乏经验的手中，可能会损坏您的系统。

## 警告 2

Portainer 插件旨在调试 Home Assistant 及其容器。它并不设计用于管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器。** 忽略这一点将使您的系统不受支持！

## 安装

要安装此插件，您首先需要前往您的个人资料并开启“高级模式”，完成后返回 Home Assistant 插件并搜索“Portainer”，并像安装其他插件一样进行安装。

要能够使用此插件，您需要禁用此插件的保护模式。没有它，插件无法访问 Docker。

1. 在监督插件商店中搜索“Portainer”插件并安装。
2. 将“保护模式”开关设置为关闭。
3. 启动“Portainer”插件。
4. 检查“Portainer”插件的日志，查看一切是否正常。

## 配置

**注意**：_记得在更改配置时重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，不要复制粘贴！创建您自己的！_

### 选项： `log_level`

`log_level` 选项控制插件输出的日志级别，可以更改为更多或更少的详细信息，这在处理未知问题时可能很有用。可能的值有：

- `trace`: 显示每个细节，例如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 并非错误的例外情况。
- `error`: 不需要立即采取行动的运行时错误。
- `fatal`: 情况非常严重。插件变得不可用。

请注意，每个级别自动包括更严重级别的日志消息，例如 `debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在排除故障。

### 选项： `agent_secret`

设置共享代理密钥的选项。也必须在远程代理中作为环境变量进行设置。

## 更新日志与发布

本存储库使用 [GitHub 的发布][releases] 功能维护变更日志。

发布基于 [语义化版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 格式。简单来说，版本将根据以下内容递增：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几种选择可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord]，用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha]，用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子论坛][reddit] 在 [/r/homeassistant][reddit]。

您也可以在这里 [打开一个问题][issue] GitHub。

## 作者与贡献者

该存储库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此授予任何获得本软件及相关文档文件（“软件”）副本的人免费、无条件使用该软件的权利，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或销售该软件副本的权利，以及允许向其提供软件的人这样做，受到以下条件的限制：

上述版权声明和本许可证声明应包含在所有副本或软件的实质性部分中。

该软件是按“现状”提供的，不提供任何形式的担保，明示或暗示，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有人都不对由于使用该软件或与该软件的使用或其他交易有关的任何索赔、损害或其他责任承担责任，无论是在合同、侵权或其他方面。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm