# Home Assistant 社区插件：Portainer

Portainer 是一个开源的轻量级管理用户界面，可以让您轻松管理 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件非常强大，可以让您访问几乎整个系统。虽然这个插件是经过仔细创建和维护的，并考虑到安全性，但在错误或没有经验的用户手中，可能会对您的系统造成损害。

## 警告 2

Portainer 插件旨在调试 Home Assistant 及其容器。它并不旨在或设计用于管理或部署您的自定义软件或第三方容器。

**Home Assistant 不支持在 Home Assistant OS 或监督安装类型上运行第三方容器。** 忽视这一点，将使您的系统变为不受支持！

## 安装

要安装此插件，首先需要进入您的个人资料并开启“高级模式”，完成后返回 Home Assistant 插件并搜索“Portainer”，并像安装其他插件一样安装它。

要能够使用此插件，您需要在此插件上禁用保护模式。没有它，插件无法访问 Docker。

1. 在 Supervisor 插件商店中搜索“Portainer”插件并安装它。
2. 将“保护模式”开关设置为关闭。
3. 启动“Portainer”插件。
4. 检查“Portainer”插件的日志，以查看一切是否正常。

## 配置

**注意**：_修改配置后，请记得重启插件。_

插件配置示例：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，不要直接复制粘贴！请创建您自己的！_

### 选项：`log_level`

`log_level` 选项控制插件的日志输出级别，可以更改为更详细或更简洁，这在处理未知问题时可能会很有用。可能的值包括：

- `trace`：显示所有细节，比如调用的所有内部函数。
- `debug`：显示详细的调试信息。
- `info`：正常（通常）有趣的事件。
- `warning`：非错误的异常事件。
- `error`：不需要立即处理的运行时错误。
- `fatal`：发生了非常严重的错误。插件变得不可用。

请注意，每个级别自动包括来自更严重级别的日志消息，例如，`debug` 也会显示 `info` 消息。默认情况下，`log_level` 设置为 `info`，这是推荐的设置，除非您在故障排除。

### 选项：`agent_secret`

设置共享代理密钥的选项。也必须在远程代理中作为环境变量设置。

## 更新日志与发行版

该代码库使用 [GitHub 的发行版][releases] 功能维护变更日志。

发行版基于 [语义版本控制][semver]，使用 `MAJOR.MINOR.PATCH` 的格式。简言之，版本号将根据以下因素增加：

- `MAJOR`：不兼容或重大更改。
- `MINOR`：向后兼容的新功能和增强。
- `PATCH`：向后兼容的 bug 修复和包更新。

## 支持

有问题吗？

您有几种选择可以得到解答：

- [Home Assistant 社区插件 Discord 聊天服务器][discord]，用于插件支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha]，用于一般的 Home Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [/r/homeassistant][reddit] 的 [Reddit 子版块][reddit]。

您也可以在这里 [打开一个问题][issue] GitHub。

## 作者与贡献者

此代码库的最初设置由 [Franck Nijhof][frenck] 提供。

要查看所有作者和贡献者的完整列表，请查看 [贡献者页面][contributors]。

## 许可证

MIT 许可证

版权 (c) 2018-2021 Franck Nijhof

在此特此授予获得本软件及相关文档文件（“软件”）副本的任何人免费使用该软件的权利，不受限制，包括无限制地使用、复制、修改、合并、发布、分发、再许可和/或出售软件的副本，并允许向其提供软件的人这样做，需遵循以下条件：

上述版权声明和此许可声明应包含在所有副本或软件的实质部分中。

该软件是按“原样”提供的，不提供任何形式的担保，无论明示或暗示，包括但不限于对适销性、特定用途的适合性和不侵权的担保。在任何情况下，作者或版权持有者均不对因使用或其他交易而引起的任何索赔、损害或其他责任承担责任，无论是合同、侵权或其他方式的原因。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm