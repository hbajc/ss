# Home Assistant Community Add-on: Tor

[![Release][release-shield]][release] ![项目阶段][project-stage-shield] ![项目维护][maintenance-shield]

[![Discord][discord-shield]][discord] [![社区论坛][forum-shield]][forum]

[![通过 GitHub Sponsors 支持 Frenck][github-sponsors-shield]][github-sponsors]

[![在 Patreon 上支持 Frenck][patreon-shield]][patreon]

保护您的隐私并通过 Tor 访问 Home Assistant。

## 关于

这个 Tor 插件允许您将 Home Assistant 实例作为 Onion 站点访问，
通过 [Tor 的隐秘服务][tor-hidden-service] 功能。启用此功能后，
您不需要打开防火墙端口或设置 HTTPS 来实现安全的远程访问。

如果您想要以下功能，这很有用：

- 远程访问您的 Home Assistant 实例，而无需打开防火墙端口
  或设置 VPN。
- 不想或者不知道如何获取 SSL/TLS 证书以及 HTTPS
  配置。
- 想要阻止攻击者访问/扫描您的端口和
  服务器。
- 想要阻止任何人知道您的家庭 IP 地址并看到您与
  Home Assistant 的流量。

该插件还提供了打开 Sock 代理到
Tor 网络的功能。允许您通过 Home Assistant 安装从任何（支持 SOCKS 的）
应用程序访问 Tor。

[discord-shield]: https://img.shields.io/discord/478094546522079232.svg
[discord]: https://discord.me/hassioaddons
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/t/home-assistant-community-add-on-tor/33822?u=frenck
[github-sponsors-shield]: https://frenck.dev/wp-content/uploads/2019/12/github_sponsor.png
[github-sponsors]: https://github.com/sponsors/frenck
[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[patreon-shield]: https://frenck.dev/wp-content/uploads/2019/12/patreon.png
[patreon]: https://www.patreon.com/frenck
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
[release-shield]: https://img.shields.io/badge/version-v6.0.1-blue.svg
[release]: https://github.com/hassio-addons/addon-tor/tree/v6.0.1
[tor-hidden-service]: https://www.torproject.org/docs/hidden-services.html.en