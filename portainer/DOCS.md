# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理用户界面，可以让您轻松管理一个或多个 Docker 主机或 Docker swarm 集群。

管理 Docker 从未如此简单。Portainer 提供了详细的 Docker 概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件非常强大，可以让您访问几乎整个系统。尽管这个插件是在注意安全的情况下创建和维护的，但在错误或缺乏经验的人手中，可能会损害您的系统。

## 警告 2

Portainer 插件旨在调试 Home Assistant 及其容器。它并不是为了管理或部署您的自定义软件或第三方容器而设计的。

**Home Assistant 不支持在 Home Assistant 操作系统或监督安装类型上运行第三方容器**。忽略这一点将使您的系统被视为不支持！

## 安装

要安装此插件，您需要先转到您的个人资料并启用 “高级模式”，完成后返回 Home Assistant 插件并搜索 “Portainer”，然后像安装其他插件一样安装它。

为了能够使用此插件，您需要禁用此插件的保护模式。没有它，插件无法访问 Docker。

1. 在 Supervisor 插件商店中搜索 “Portainer” 插件并安装它。
1. 将“保护模式”开关设置为关闭。
1. 启动 “Portainer” 插件。
1. 检查 “Portainer” 插件的日志，以查看一切是否顺利。

## 配置

**注意**：_更改配置时，请记得重新启动插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: 密码
```

**注意**：_这只是一个示例，不要复制和粘贴它！创建您自己的！_

### 选项: `log_level`

`log_level` 选项控制插件的日志输出级别，可以根据需要更改为更详细或更简洁，这在处理未知问题时可能很有用。可能的值有：

- `trace`: 显示每个细节，如所有被调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不错误的特殊情况。
- `error`: 不需要立即采取行动的运行时错误。
- `fatal`: 出现严重问题，插件无法使用。

请注意，每个级别自动包含来自更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在排除故障。

### 选项: `agent_secret`

用于设置共享代理秘密的选项。必须在远程代理中也作为环境变量设置。

## 更新日志和发布

该存储库使用 [GitHub 的发布][releases] 功能保持变更日志。

发布基于 [语义版本控制][semver]，并使用 `MAJOR.MINOR.PATCH` 的格式。简而言之，版本将基于以下内容进行递增：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 兼容向后新的特性和增强。
- `PATCH`: 兼容向后的错误修复和包更新。

## 支持

有问题吗？

您有几种选择可以得到答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 论坛][reddit] 在 [/r/homeassistant][reddit]。

您也可以在这里 [开一个问题][issue] GitHub。

## 作者和贡献者

该存储库的初始设置由 [Franck Nijhof][frenck] 创建。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此免费授权任何获取本软件及相关文档文件（“软件”）副本的人，对软件进行无限制的处理，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许提供软件的人这样做，受以下条件约束：

上述版权声明和此许可声明应包含在所有软件副本或重要部分中。

本软件是“按原样”提供的，不附有任何类型的担保，无论是明示或暗示，包括但不限于对适销性、特定目的适用性和不侵权的担保。在任何情况下，作者或版权持有人对任何索赔、损害或其他责任不承担责任，无论是在合同、侵权还是其他方面，由于软件或与软件的使用或其他交易而引起的。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm