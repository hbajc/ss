# ESPHome 开发版插件

这是 **开发** 版本的 ESPHome 插件。

要部署生产节点，请使用主流发布插件。

该插件使用每天 02:00 UTC 自动构建的 ESPHome 版本，用于测试开发中的组件。请参见下面的 `esphome_fork` 配置以正确配置插件。一旦更新配置，请确保重建镜像。

## 配置

**注意**：_记住在更改配置时重新启动插件。_

### 选项： `esphome_fork`

从一个分叉或分支安装 ESPHome。
例如，要测试一个拉取请求，请使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者你可以指定分叉拥有者的用户名和分支 `username:branch`，这
假设该仓库仍然名为 `esphome`。

如果你需要在镜像更新之前测试 dev 分支的最新提交，可以在此处输入 `dev`。

请注意，你使用的分叉或分支 **必须** 与 ESPHome dev 保持最新，
否则插件 **将无法启动**。

## 一般 ESPHome 插件配置

在其他版本中也有可用的一般选项。

### 选项： `ssl`

启用或禁用对该插件的Web服务器的加密 SSL/TLS (HTTPS) 连接。
将其设置为 `true` 来加密通信，否则设置为 `false`。
请注意，如果将其设置为 `true`，你还必须生成加密所需的密钥和证书
文件。例如使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项： `certfile`

用于SSL的证书文件。如果该文件不存在，则插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项： `keyfile`

用于SSL的私钥文件。如果该文件不存在，则插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项： `leave_front_door_open`

将此选项添加到插件配置中，允许你通过将其设置为 `true` 来禁用
身份验证。

### 选项： `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以集成
到现有的 Web 代理中，例如 NGINX 下的相对 URL。默认值为 `/`。

### 选项： `status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。这在不同子网之间
不起作用，除非你的路由器支持 mDNS 转发或 avahi。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。 如果所有节点即使在连接时也始终显示离线状态，请使用此选项。

### 选项： `streamer_mode`

如果设置为 `true`，这将启用流媒体模式，使 ESPHome 隐藏所有
潜在的私人信息。例如 WiFi (B)SSIDs (可能会被用来查找你的位置信息)、用户名等。请注意，你需要在 YAML 文件中使用
`!secret` 标签，以防止在编辑和验证时也显示这些信息。