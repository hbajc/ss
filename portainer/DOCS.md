# Home Assistant Community Add-on: Portainer

Portainer 是一个开源的轻量级管理用户界面，使您能够
轻松管理一个或多个 Docker 主机或 Docker 集群。

管理 Docker 从未如此简单。Portainer 提供了 Docker 的详细
概述，并允许您管理容器、镜像、网络和卷。

## 警告 1

Portainer 插件非常强大，几乎可以访问您整个系统。尽管此插件是在小心和
重视安全的情况下创建和维护的，但在错误或缺乏经验的用户手中，
它可能会对您的系统造成损害。

## 警告 2

Portainer 插件旨在调试 Home Assistant 及其容器。
它并不是为了管理或部署您的自定义软件
或第三方容器而设计的。

**Home Assistant 不支持在 Home Assistant 操作系统或主控安装类型上运行第三方容器。**
忽略这一点将使您的系统变为不受支持！

## 安装

要安装此插件，您首先需要转到您的个人资料并启用
“高级模式”，完成后返回 Home Assistant 插件并搜索
“Portainer”并像安装其他任何插件一样安装它。

要能够使用此插件，您需要在此插件上禁用保护模式。
没有它，插件将无法访问 Docker。

1. 在 Supervisor 插件商店中搜索“Portainer”插件并
   安装它。
1. 将“保护模式”开关设置为关闭。
1. 启动“Portainer”插件。
1. 检查“Portainer”插件的日志，以查看是否一切正常。

## 配置

**注意**：_在更改配置时，请记得重启插件。_

示例插件配置：

```yaml
log_level: info
agent_secret: password
```

**注意**：_这只是一个示例，请不要复制粘贴！创建您自己的！_

### 选项： `log_level`

`log_level` 选项控制插件的日志输出级别，可以
更改为更多或更少的详细信息，这可能在您处理
未知问题时很有用。可能的值包括：

- `trace`: 显示每个细节，例如所有调用的内部函数。
- `debug`: 显示详细的调试信息。
- `info`: 正常（通常）有趣的事件。
- `warning`: 不属于错误的特殊情况。
- `error`: 不需要立即采取行动的运行时错误。
- `fatal`: 发生了严重错误。插件变得无法使用。

请注意，每个级别自动包含来自更高严峻级别的日志消息，
例如，`debug` 还会显示 `info` 消息。默认情况下，
`log_level` 设置为 `info`，这是推荐设置，除非您在进行故障排除。

### 选项： `agent_secret`

设置共享代理密钥的选项。也必须在远程代理中
作为环境变量设置。

## 更新日志与版本

此存储库使用 [GitHub 的发布][releases]
功能保持更新日志。

版本基于 [语义版本控制][semver]，并使用格式
`MAJOR.MINOR.PATCH`。总而言之，版本将根据以下内容递增：

- `MAJOR`: 不兼容或重大更改。
- `MINOR`: 向后兼容的新特性和增强。
- `PATCH`: 向后兼容的错误修复和软件包更新。

## 支持

有问题？

您有几种方式可以得到答案：

- [Home Assistant Community Add-ons Discord 聊天服务器][discord] 用于插件
  支持和功能请求。
- [Home Assistant Discord 聊天服务器][discord-ha] 用于一般 Home
  Assistant 讨论和问题。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 子版块][reddit] 在 [/r/homeassistant][reddit]

您还可以在这里 [提起一个问题][issue] GitHub。

## 作者与贡献者

该存储库的最初设置由 [Franck Nijhof][frenck] 完成。

要查看所有作者和贡献者的完整列表，
请检查 [贡献者页面][contributors]。

## 许可

MIT 许可证

版权 (c) 2018-2021 Franck Nijhof

特此免费授予任何获得该软件及其相关文档文件（“软件”）副本的人，
不受限制地处理该软件，包括但不限于使用、复制、修改、合并、出版、分发、
再许可和/或出售该软件副本的权利，并允许获得该软件的人这样做，须遵循以下条件：

上述版权声明和此许可声明应包含在所有
副本或该软件的实质性部分中。

该软件按“原样”提供，不附有任何形式的保证，无论是明示的还是默示的，
包括但不限于适销性、特定用途的适用性和不侵权的保证。在任何情况下，作者或版权
持有人均不对因使用该软件或与软件有关的使用或其他交易而引起的任何索赔、损害或其他
责任承担责任，无论是在合同诉讼、侵权或其他诉讼中。

[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord]: https://discord.me/hassioaddons
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[reddit]: https://reddit.com/r/homeassistant
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[semver]: http://semver.org/spec/v2.0.0.htm