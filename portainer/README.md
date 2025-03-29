# Home Assistant社区插件：Portainer

[![GitHub Release][releases-shield]][releases]
![项目阶段][project-stage-shield]
[![许可证][license-shield]](LICENSE.md)

![支持aarch64架构][aarch64-shield]
![支持amd64架构][amd64-shield]
![支持armhf架构][armhf-shield]
![支持armv7架构][armv7-shield]
![支持i386架构][i386-shield]

[![Github Actions][github-actions-shield]][github-actions]
![项目维护][maintenance-shield]
[![GitHub活动][commits-shield]][commits]

[![Discord][discord-shield]][discord]
[![社区论坛][forum-shield]][forum]

[![通过GitHub赞助Frenck][github-sponsors-shield]][github-sponsors]

[![在Patreon上支持Frenck][patreon-shield]][patreon]

轻松管理您的Docker环境。

![Portainer Hass.io插件](images/screenshot.png)

## 关于

Portainer是一个开源的轻量级管理用户界面，允许您轻松管理Docker主机或Docker swarm集群。

管理Docker从未如此简单。Portainer提供了Docker的详细概述，允许您管理容器、镜像、网络和卷。

[:books: 阅读完整的插件文档][docs]

## 分支项目

此插件已被其作者停止维护，不再在社区库中提供。
这是一个尽力而为的分支项目。

如果您运行Home Assistant，请注意，运行额外的容器
不是支持的用例，并将导致您的系统被标记为不受支持。

## 警告 1

Portainer插件非常强大，几乎可以访问您整个系统。尽管这个插件是在小心和考虑安全的情况下创建和维护的，但在不当或缺乏经验的操作下，
它可能会损坏您的系统。

## 警告 2

Portainer插件旨在调试Home Assistant及其容器。
它并不是为了管理或部署您的自定义软件或第三方容器而设计的。

**Home Assistant不支持在Home Assistant OS或监督安装类型上运行第三方容器**
。忽视这一点，将使您的系统被标记为不受支持！

## 支持

有问题吗？

[在这里打开一个问题][issue] GitHub。

## 贡献

这是一个活跃的开源项目。我们始终欢迎希望使用或贡献代码的人。

我们已设置一个单独的文档，包含我们的
[贡献指南](,github/CONTRIBUTING.md)。

感谢您的参与！ :heart_eyes:

## 作者和贡献者

该库的原始设置由[Franck Nijhof][frenck]完成。

要查看所有作者和贡献者的完整名单，
请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权 (c) 2018-2021 Franck Nijhof

特此授予任何获得本软件及相关文档文件（“软件”）副本的人，在不受限制的情况下处理软件，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售软件副本的权利，并允许向其提供软件的人这样做，受以下条件限制：

上述版权声明和本许可声明应包含在软件的所有副本或实质部分中。

软件是“按原样”提供的，不附任何形式的担保，无论是明示还是暗示，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权所有者均不对任何索赔、损害或其他责任承担责任，无论是在合同诉讼、侵权或其他情况下，而是因软件或与软件的使用或其他交易相关。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[commits-shield]: https://img.shields.io/github/commit-activity/y/hassio-addons/addon-portainer.svg
[commits]: https://github.com/hassio-addons/addon-portainer/commits/main
[contributors]: https://github.com/hassio-addons/addon-portainer/graphs/contributors
[discord-ha]: https://discord.gg/c5DvZ4e
[discord-shield]: https://img.shields.io/discord/478094546522079232.svg
[discord]: https://discord.me/hassioaddons
[docs]: https://github.com/hassio-addons/addon-portainer/blob/main/portainer/DOCS.md
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer/68836?u=frenck
[frenck]: https://github.com/frenck
[github-actions-shield]: https://github.com/hassio-addons/addon-portainer/workflows/CI/badge.svg
[github-actions]: https://github.com/hassio-addons/addon-portainer/actions
[github-sponsors-shield]: https://frenck.dev/wp-content/uploads/2019/12/github_sponsor.png
[github-sponsors]: https://github.com/sponsors/frenck
[i386-shield]: https://img.shields.io/badge/i386-no-red.svg
[issue]: https://github.com/hassio-addons/addon-portainer/issues
[license-shield]: https://img.shields.io/github/license/hassio-addons/addon-portainer.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2021.svg
[patreon-shield]: https://frenck.dev/wp-content/uploads/2019/12/patreon.png
[patreon]: https://www.patreon.com/frenck
[project-stage-shield]: https://img.shields.io/badge/project%20stage-%20!%20DEPRECATED%20%20%20!-ff0000.svg
[reddit]: https://reddit.com/r/homeassistant
[releases-shield]: https://img.shields.io/github/release/hassio-addons/addon-portainer.svg
[releases]: https://github.com/hassio-addons/addon-portainer/releases
[repository]: https://github.com/hassio-addons/repository