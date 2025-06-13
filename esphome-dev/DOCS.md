# ESPHome 开发版本插件

这是 **开发** 版本的 ESPHome 插件。

要部署生产节点，请使用主流发布插件。

该插件使用一个每天在 UTC 时间 02:00 自动构建的 ESPHome 版本，主要用于测试开发中的组件。请查看下面的 `esphome_fork` 配置，以正确配置插件。在更新配置后，请确保重新构建镜像。

## 配置

**注意**：_配置更改时，请记得重启插件。_

### 选项: `esphome_fork`

从一个分支或分叉安装 ESPHome。
例如，要测试一个拉取请求，请使用 `pull/XXXX/head`，这里 `XXXX` 是 PR 号，
或者您可以指定分叉拥有者的用户名和分支 `username:branch`，这假设
该仓库仍然名为 `esphome`。

如果您需要测试在图像更新之前的开发分支的最新提交，可以在此处输入 `dev`。

请注意，您使用的分叉或分支 **必须** 与 ESPHome 开发版本保持最新，
否则插件 **将无法启动**。

## 一般 ESPHome 插件配置

其他版本也提供一般选项。

### 选项: `ssl`

启用或禁用对该插件的 Web 服务器的加密 SSL/TLS (HTTPS) 连接。
将其设置为 `true` 以加密通讯，设置为 `false` 则为不加密。
请注意，如果您将其设置为 `true`，您还必须生成加密所需的密钥和证书文件。
例如使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项: `certfile`

用于 SSL 的证书文件。如果此文件不存在，插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项: `keyfile`

用于 SSL 的私钥文件。如果此文件不存在，插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项: `leave_front_door_open`

将此选项添加到插件配置中，可以通过将其设置为 `true` 来禁用身份验证。

### 选项: `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以在现有的 Web 代理（如 NGINX）中集成相对 URL。默认为 `/`。

### 选项: `status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。如果路由器不支持 mDNS 转发或 avahi，则这一功能在子网之间无法工作。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点在连接时仍显示离线状态，请使用此设置。

### 选项: `streamer_mode`

如果设置为 `true`，则启用串流模式，这将使 ESPHome 隐藏所有潜在的私人信息。
例如，WiFi (B)SSID（可能会用于查找您的位置），用户名等。请注意，您需要在 YAML 文件中使用
`!secret` 标签，以避免在编辑和验证时显示这些信息。