# Home Assistant 社区附加组件：Z-Wave JS UI

[![Release][release-shield]][release] ![Project Stage][project-stage-shield] ![Project Maintenance][maintenance-shield]

[![Discord][discord-shield]][discord] [![Community Forum][forum-shield]][forum]

[![Sponsor Frenck via GitHub Sponsors][github-sponsors-shield]][github-sponsors]

[![Support Frenck on Patreon][patreon-shield]][patreon]

完全可配置的 Z-Wave JS 控制面板和 MQTT 网关。

![Z-Wave JS UI][logo]

## 关于

Z-Wave JS UI 附加组件提供了一个额外的控制面板，允许您配置 Z-Wave 网络的每个方面。它提供了一个解耦的网关，可以使用 Z-Wave JS WebSockets（被 Home Assistant Z-Wave JS 集成使用）和 MQTT 进行通信（甚至可以同时进行）。

一些优势和使用案例：

- 与 Home Assistant Z-Wave JS 集成兼容。
- 您的 Z-Wave 网络将在 Home Assistant 重启之间继续运行。
- 您可以直接使用 Node-RED 等工具与您的 Z-Wave 网络进行交互，同时它也可供 Home Assistant 使用。
- 允许基于 [ESPHome.io][esphome] 的 ESP 设备直接响应或与您的 Z-Wave 网络协作。
- 当找到 Mosquitto 附加组件时，会自动进行预配置。

该附加组件使用 [Z-Wave JS UI][zwave-js-ui] 软件。

[discord-shield]: https://img.shields.io/discord/478094546522079232.svg
[discord]: https://discord.me/hassioaddons
[esphome]: https://esphome.io/components/mqtt.html#on-message-trigger
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg
[forum]: https://community.home-assistant.io/?u=frenck
[github-sponsors-shield]: https://frenck.dev/wp-content/uploads/2019/12/github_sponsor.png
[github-sponsors]: https://github.com/sponsors/frenck
[logo]: https://github.com/hassio-addons/addon-zwave-js-ui/raw/main/zwave-js-ui/logo.png
[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[patreon-shield]: https://frenck.dev/wp-content/uploads/2019/12/patreon.png
[patreon]: https://www.patreon.com/frenck
[project-stage-shield]: https://img.shields.io/badge/project%20stage-production%20ready-brightgreen.svg
[release-shield]: https://img.shields.io/badge/version-v4.1.1-blue.svg
[release]: https://github.com/hassio-addons/addon-zwave-js-ui/tree/v4.1.1
[zwave-js-ui]: https://github.com/zwave-js/zwave-js-ui