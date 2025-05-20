# ESPHome 开发版插件

这是 ESPHome 插件的 **开发** 版本。

要部署生产节点，请使用主流发布插件。

该插件使用的 ESPHome 版本每天在 UTC 时间 02:00 自动构建，用于测试开发中的组件。请查看下面的 `esphome_fork` 配置以正确配置插件。更新配置后，请确保重建映像。

## 配置

**注意**：_更改配置时，请记得重新启动插件。_

### 选项：`esphome_fork`

从分支或分支安装 ESPHome。
例如，要测试拉取请求，请使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定分支所有者的用户名和分支 `username:branch`，假设
该存储库仍名为 `esphome`。

如果您需要在映像更新之前测试开发分支上的最新提交，可以在此处输入 `dev`。

请注意，您使用的分支或分支 **必须** 与 ESPHome 开发版保持最新
否则插件 **将无法启动**。

## 一般 ESPHome 插件配置

一般选项也可在其他版本中使用。

### 选项：`ssl`

启用或禁用对该插件的 Web 服务器的加密 SSL/TLS（HTTPS）连接。
将其设置为 `true` 以加密通信，反之则为 `false`。
请注意，如果您将其设为 `true`，还必须生成用于加密的密钥和证书
文件。可以使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项：`certfile`

用于 SSL 的证书文件。如果该文件不存在，则插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项：`keyfile`

用于 SSL 的私钥文件。如果该文件不存在，则插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项：`leave_front_door_open`

将此选项添加到插件配置中可以通过将其设置为 `true` 来禁用
身份验证。

### 选项：`relative_url`

在相对 URL 下托管 ESPHome 仪表板，这样它可以集成到现有的 Web 代理中，比如 NGINX 的相对 URL。默认为 `/`。

### 选项：`status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。这在子网之间
是无法工作的，除非您的路由器支持 mDNS 转发或 avahi。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点即使连接时也始终显示离线状态，请使用此选项。

### 选项：`streamer_mode`

如果设置为 `true`，这将启用流模式，使 ESPHome 隐藏所有
潜在的私人信息。例如 WiFi (B)SSIDs（可能用于找到您的位置）、用户名等。请注意，在编辑和验证时，您需要在 YAML 文件中使用
`!secret` 标签以防止这些信息显示出来。