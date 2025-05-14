# Home Assistant Community Add-on: Portainer

Portainer 是一个开源轻量级管理界面，允许您轻松管理 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件功能强大，可以访问您几乎整个系统。尽管这个插件是在安全意识下精心创建和维护的，但在错误或经验不足的手中，它可能会损坏您的系统。

## 警告 2

Portainer 插件的目的是用于调试 Home Assistant 及其容器。它并不意味着或设计用于管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器。**忽视这一点，将使您的系统被视为不受支持！

## 安装

要安装此插件，您首先需要进入您的个人资料并开启“高级模式”，完成后返回 Home Assistant 插件并搜索“Portainer”，然后像安装其他插件一样安装它。

要能使用此插件，您需要禁用该插件上的保护模式。没有此选项，插件将无法访问 Docker。

1. 在监控器插件商店中搜索“Portainer”插件并安装。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”插件。
1. 检查“Portainer”插件的日志，查看是否一切正常。

## 配置

**注意**：_在更改配置时，请记得重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，不要直接复制粘贴！请创建您自己的配置！_

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这可能在处理未知问题时很有用。可能的值包括：

- `trace`: 显示每一个细节，如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 异常情况但不是错误。
- `error`: 运行时错误，但不需要立即采取行动。
- `fatal`: 某些事情出了严重问题。插件变得不可用。

请注意，每个级别自会包含更严重级别的日志消息，例如 `debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在进行故障排除。

### 选项: `agent_secret`

设置共享代理密钥的选项。也必须在远程代理中作为环境变量设置。

## 更新日志与发布

本存储库使用 [GitHub 的 releases][releases] 功能维护变更日志。

发布基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将根据以下情况进行递增：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新功能和增强。
- `PATCH`: 向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有几种选择可以获得答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]。

您也可以在这里 [打开问题][issue] GitHub。

## 作者与贡献者

本存储库的最初设置由 [Franck Nijhof][frenck] 完成。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2018-2021 Franck Nijhof

特此免费授权任何获得本软件及相关文档文件（“软件”）副本的人，在不受限制的情况下处理该软件，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或销售该软件的副本，并允许提供软件的人如此处理，受以下条件的约束：

上述版权声明和本许可证声明应包含在所有副本或实质部分中。

本软件按“原样”提供，不附带任何担保，无论是明示或暗示，包括但不限于适销性、特定用途适用性和不侵权的担保。在任何情况下，作者或版权持有人对因使用本软件或与本软件有关的其他交易而产生的任何索赔、损害或其他责任不承担任何责任，无论是基于合同、侵权或其他情况。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm