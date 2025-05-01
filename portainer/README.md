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

Portainer是一个开源的轻量级管理界面，使您能够轻松管理Docker主机或Docker集群。

管理Docker从未如此简单。Portainer提供了详细的Docker概述，允许您管理容器、镜像、网络和卷。

[:books: 阅读完整的插件文档][docs]


## FORKED

该插件已由其作者停止维护，并且在社区仓库中不再可用。
这是一个尽力而为的分叉。

如果您运行Home Assistant，请注意运行其他容器并不是支持的用例，并且会导致您的系统被标记为不受支持。

## 警告1

Portainer插件非常强大，几乎可以访问您整个系统。虽然该插件是经过仔细创建和维护并考虑到安全性的，但在不当或缺乏经验的手中，它可能会损坏您的系统。

## 警告2

Portainer插件旨在用于调试Home Assistant及其容器。
它并不是用于管理或部署您的自定义软件或第三方容器。

**Home Assistant不支持在Home Assistant OS或监督安装类型上运行第三方容器。**
忽略这一点，将使您的系统被标记为不受支持！

## 支持

有问题吗？

[在这里提交问题][issue]到GitHub。

## 贡献

这是一个活跃的开源项目。我们始终欢迎希望使用代码或对其做出贡献的人。

我们已经设置了一个包含我们[贡献指南](,github/CONTRIBUTING.md)的单独文档。

感谢您的参与！:heart_eyes:

## 作者与贡献者

该存储库的最初设置由[Franck Nijhof][frenck]完成。

要查看所有作者和贡献者的完整列表，请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权 (c) 2018-2021 Franck Nijhof

特此免费授权，任何获得本软件及其相关文档文件（“软件”）副本的人，可以不受限制地处理软件，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或出售软件副本的权利，并允许提供软件的人这样做，条件是必须遵守以下条件：

上述版权声明和本许可声明应包含在所有软件副本或重大部分中。

软件按“原样”提供，不提供任何种类的保证，明示或暗示，包括但不限于对适销性、特定用途的适合性及不侵权的保证。在任何情况下，作者或版权持有人均不对因使用软件或其他交易而造成的任何索赔、损害或其他责任承担责任，无论是在合同、侵权或其他方面。

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