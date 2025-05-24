# ESPHome 开发版附加组件

这是 **开发** 版本的 ESPHome 附加组件。

要部署生产节点，请使用主流发布的附加组件。

该附加组件使用每天在协调世界时间 02:00 自动构建的 ESPHome 版本，用于测试开发中的组件。请参见下面的 `esphome_fork` 配置来正确配置附加组件。一旦更新配置，请确保重建镜像。

## 配置

**注意**：_更改配置时，请记得重启附加组件。_

### 选项： `esphome_fork`

从一个分叉或分支安装 ESPHome。
例如，要测试一个拉取请求，可以使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，或者可以指定分叉所有者的用户名和分支 `username:branch`，这假设仓库仍然命名为 `esphome`。

如果您需要在镜像更新之前测试开发分支上的最新提交，可以在此输入 `dev`。

请注意，您使用的分叉或分支 **必须** 与 ESPHome 开发保持最新，否则附加组件 **将不会启动**。

## 一般 ESPHome 附加组件配置

在其它版本中也可以使用的一般选项。

### 选项： `ssl`

启用或禁用与该附加组件的Web服务器之间的加密 SSL/TLS (HTTPS) 连接。
设置为 `true` 以加密通信，设置为 `false` 否则。
请注意，如果将其设置为 `true`，则还必须生成加密所需的密钥和证书文件。可以使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/) 或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项： `certfile`

用于 SSL 的证书文件。如果该文件不存在，则附加组件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项： `keyfile`

用于 SSL 的私钥文件。如果该文件不存在，则附加组件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项： `leave_front_door_open`

向附加组件配置中添加此选项允许您通过将其设置为 `true` 来禁用身份验证。

### 选项： `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以在现有的 Web 代理（如 NGINX）下集成到相对 URL 中。默认为 `/`。

### 选项： `status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。除非您的路由器支持 mDNS 转发或 avahi，否则这在子网之间无法工作。

将其设置为 `true` 将使 ESPHome 使用 ICMP ping 请求获取节点状态。如果所有节点在连接时始终显示离线状态，请使用此选项。

### 选项： `streamer_mode`

如果设置为 `true`，则将启用流媒体模式，使 ESPHome 隐藏所有潜在的私人信息。例如 WiFi (B)SSIDs（可能用于查找您的位置）、用户名等。请注意，您需要在 YAML 文件中使用 `!secret` 标签来防止这些在编辑和验证时显示。