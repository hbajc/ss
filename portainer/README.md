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

[![通过GitHub Sponsors支持Frenck][github-sponsors-shield]][github-sponsors]

[![在Patreon上支持Frenck][patreon-shield]][patreon]

轻松管理你的Docker环境。

![Portainer Hass.io插件](images/screenshot.png)

## 关于

Portainer是一个开源轻量级管理界面，让你可以
轻松地管理Docker主机或Docker swarm集群。

管理Docker从未如此简单。Portainer提供了Docker的详细
概述，并允许你管理容器、镜像、网络和
卷。

[:books: 阅读完整的插件文档][docs]

## FORKED

此插件已由其作者停止维护，不再可从Community存储库获取。
这是一个尽力而为的fork。

如果你运行Home Assistant，请注意，运行额外的容器
并不是一个支持的用例，并且会使你的系统被标记为
不受支持。

## 警告 1

Portainer插件非常强大，几乎可以访问
你整个系统。虽然这个插件是经过细心创建和维护的，
并考虑了安全性，但在错误或缺乏经验的手中，
可能会对你的系统造成损害。

## 警告 2

Portainer插件旨在调试Home Assistant及其容器。
它并非旨在或设计用于管理或部署你的自定义软件
或第三方容器。

**Home Assistant不支持在Home Assistant操作系统或
监督安装类型上运行第三方容器。**
忽视这一点，将会使你的系统被视为不受支持！

## 支持

有问题吗？

[在这里提交问题][issue] GitHub。

## 贡献

这是一个活跃的开源项目。我们始终欢迎希望
使用代码或对其做出贡献的人。

我们已设置了一个单独的文档，其中包含我们的
[贡献指南](,github/CONTRIBUTING.md)。

感谢您的参与！ :heart_eyes:

## 作者与贡献者

此存储库的最初设置由[Franck Nijhof][frenck]完成。

要查看所有作者和贡献者的完整列表，
请查看[贡献者页面][contributors]。

## 许可证

MIT许可证

版权所有 (c) 2018-2021 Franck Nijhof

特此免费授权任何获得本软件及相关文档文件（"软件"）副本的个人，在不受限制的情况下处理
软件，包括但不限于使用、复制、修改、合并、发布、分发、再授权和/或销售
软件的副本，并允许向其提供软件的人这样做，受以下条件的限制：

上述版权声明和本许可声明应包含在
软件的所有副本或实质性部分中。

本软件按"原样"提供，不作任何形式的明示或
暗示担保，包括但不限于对适销性、
特定用途的适用性和非侵权的担保。在任何情况下，
作者或版权持有者均不对因使用
本软件或与本软件的使用或其他交易相关的任何
索赔、损害或其他责任负责。

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