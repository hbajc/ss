# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理界面，可以让您轻松管理 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件非常强大，并几乎可以访问您的整个系统。尽管该插件是在谨慎和考虑安全的情况下创建和维护的，但在不当或缺乏经验的情况下，它可能会损坏您的系统。

## 警告 2

Portainer 插件旨在用于调试 Home Assistant 及其容器。它并不适合或设计用于管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器。** 忽视这一点将使您的系统处于不支持状态！

## 安装

要安装此插件，首先需要进入您的个人资料并开启“高级模式”，完成后返回 Home Assistant 插件页面，搜索“Portainer”并像安装其他插件一样安装它。

要能够使用此插件，您需要禁用该插件上的保护模式。没有它，插件将无法访问 Docker。

1. 在 Supervisor 插件商店中搜索“Portainer”插件并安装它。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”插件。
1. 检查“Portainer”插件的日志，确认一切正常。

## 配置

**注意**：_记得在更改配置时重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，别复制粘贴！自己创建！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以根据需要调整为更详细或更精简，这在处理未知问题时可能会很有用。可能的值有：

- `trace`：显示每一个细节，比如所有被调用的内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：异常情况，但不是错误。
- `error`：运行时错误，但不需要立即处理。
- `fatal`：发生了严重错误。插件变得不可用。

请注意，每个级别自动包含来自更高级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您正在进行故障排除。

### 选项：`agent_secret`

设置共享代理密钥的选项。必须在远程代理中作为环境变量也进行设置。

## 更新日志与发布

该仓库使用 [GitHub 的发行][releases] 功能维护变更日志。

发行版本基于 [语义版本控制][semver]，并使用格式 `MAJOR.MINOR.PATCH`。简而言之，版本将根据以下内容进行递增：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的错误修复和包更新。

## 支持

有问题吗？

您有多种方式可以得到解答：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 进行插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 进行一般 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 论坛][reddit] 的 [/r/homeassistant][reddit]

您也可以在这里 [提交问题][issue] GitHub。

## 作者与贡献者

该仓库的最初设置来自 [Franck Nijhof][frenck]。

有关所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2018-2021 Franck Nijhof

特此免费授予任何获得本软件及其相关文档文件（“软件”）副本的人，不受限制地处理该软件，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或出售该软件的副本，并允许向其提供该软件的人这样做，需遵守以下条件：

上述版权声明和本许可声明应包含在所有副本或软件的实质部分中。

软件是按“原样”提供的，没有任何形式的担保，无论是明示的还是暗示的，包括但不限于适销性、特定用途适用性和不侵权的担保。在任何情况下，作者或版权持有人均不对因使用该软件或与该软件的使用或其他交易而产生的任何索赔、损害或其他责任承担责任，无论是在合同诉讼、侵权诉讼还是其他诉讼中。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm