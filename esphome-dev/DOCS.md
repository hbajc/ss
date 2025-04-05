# ESPHome 开发版插件

这是 **开发** 版本的 ESPHome 插件。

要部署生产节点，请使用主流发布的插件。

该插件使用每天 UTC 时间 02:00 自动构建的 ESPHome 版本，并用于测试开发中的组件。请查看下面的 `esphome_fork` 配置以正确配置插件。一旦您更新配置，请确保重建镜像。

## 配置

**注意**：_记得在更改配置后重启插件。_

### 选项：`esphome_fork`

从分支或 fork 安装 ESPHome。
例如，要测试一个拉取请求，可以使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定 fork 拥有者的用户名和分支 `username:branch`，这假设
该仓库仍然名为 `esphome`。

如果您需要在镜像更新之前测试开发分支上的最新提交，可以在这里输入 `dev`。

请注意，您使用的 fork 或分支 **必须** 与 ESPHome 开发版保持最新
否则插件 **将无法启动**。

## 一般 ESPHome 插件配置

一般选项也在其他版本中可用。

### 选项：`ssl`

启用或禁用与该插件的网络服务器的加密 SSL/TLS (HTTPS) 连接。
将其设置为 `true` 以加密通信，设置为 `false` 否则。
请注意，如果您将其设置为 `true`，您必须生成加密所需的密钥和证书
文件。例如使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项：`certfile`

用于 SSL 的证书文件。如果该文件不存在，插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认设置。

### 选项：`keyfile`

用于 SSL 的私钥文件。如果该文件不存在，插件启动将失败。

**注意**：该文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认设置。

### 选项：`leave_front_door_open`

将此选项添加到插件配置可通过设置为 `true` 禁用
身份验证。

### 选项：`relative_url`

在相对 URL 下托管 ESPHome 控制面板，以便它可以集成
到现有的网络代理中，比如 NGINX，使用相对 URL。默认为 `/`。

### 选项：`status_use_ping`

默认情况下，控制面板使用 mDNS 检查节点是否在线。如果您的路由器支持 mDNS
转发或 avahi，否则这不会跨子网工作。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求获取节点状态。如果所有节点在连接时始终显示离线状态，请使用此选项。

### 选项：`streamer_mode`

如果设置为 `true`，这将启用流媒体模式，使 ESPHome 隐藏所有
潜在的私人信息。例如 WiFi (B)SSID（可能用于寻找您的位置）、用户名等。
请注意，您需要在 YAML 文件中使用 `!secret` 标签以防止这些信息
在编辑和验证时显示。