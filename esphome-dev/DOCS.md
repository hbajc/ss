# ESPHome 开发版插件

这是 **开发** 版本的 ESPHome 插件。

要部署生产节点，请使用主流发布的插件。

该插件使用一个在每天 UTC 时间 02:00 自动构建的 ESPHome 版本，用于测试开发中的组件。请查看下面的 `esphome_fork` 配置以正确配置插件。一旦更新了配置，请确保重新构建镜像。

## 配置

**注意**：_记得在更改配置后重启插件。_

### 选项: `esphome_fork`

从一个分支或 Fork 安装 ESPHome。
例如，要测试一个拉取请求，请使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定 Fork 拥有者的用户名和分支 `username:branch`，这假设仓库仍然命名为 `esphome`。

如果您需要在镜像更新之前测试 dev 分支的最新提交，可以在这里输入 `dev`。

请注意，您使用的 Fork 或分支 **必须** 与 ESPHome dev 保持最新，
否则插件 **将无法启动**。

## 一般ESPHome插件配置

其他版本中也可以使用的一般选项。

### 选项: `ssl`

启用或禁用与此插件的Web服务器的加密 SSL/TLS (HTTPS) 连接。
设置为 `true` 以加密通信，反之则设置为 `false`。
请注意，如果您将此设置为 `true`，您还必须生成密钥和证书文件以进行加密。例如，使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/) 或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项: `certfile`

要用于 SSL 的证书文件。如果此文件不存在，插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认路径。

### 选项: `keyfile`

要用于 SSL 的私钥文件。如果此文件不存在，插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认路径。

### 选项: `leave_front_door_open`

将此选项添加到插件配置中允许您通过设置为 `true` 来禁用身份验证。

### 选项: `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以在相对 URL 下集成到现有的 Web 代理（如 NGINX）。默认为 `/`。

### 选项: `status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。除非您的路由器支持 mDNS 转发或 avahi，否则在子网之间无法工作。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点在连接时始终显示离线状态，请使用此选项。

### 选项: `streamer_mode`

如果设置为 `true`，这将启用流媒体模式，使 ESPHome 隐藏所有潜在的私密信息。例如，WiFi (B)SSID（可能被用来找到您的位置）、用户名等。请注意，您在 YAML 文件中需要使用 `!secret` 标签来防止在编辑和验证时显示这些信息。