# ESPHome 开发版附加组件

这是 **开发** 版本的 ESPHome 附加组件。

要部署生产节点，请使用主流发布的附加组件。

该附加组件使用的版本是每天自动构建的 ESPHome 版本，时间为 UTC 02:00。并用于测试开发中的组件。请查看下面的 `esphome_fork` 配置以正确配置附加组件。更新配置后，请确保重新构建映像。

## 配置

**注意**：_记得在更改配置后重启附加组件。_

### 选项：`esphome_fork`

从一个分叉或分支安装 ESPHome。
例如，要测试一个拉取请求，可以使用 `pull/XXXX/head`，其中 `XXXX` 是 PR 编号，
或者您可以指定分叉所有者的用户名和分支 `username:branch`，这假设
仓库仍然名为 `esphome`。

如果您需要在映像更新之前测试 dev 分支上的最新提交，可以在这里输入 `dev`。

请注意，您正在使用的分叉或分支 **必须** 与 ESPHome dev 保持最新，
否则附加组件 **将无法启动**。

## 通用 ESPHome 附加组件配置

通用选项也适用于其他版本。

### 选项：`ssl`

启用或禁用对该附加组件的 Web 服务器的加密 SSL/TLS (HTTPS) 连接。
设置为 `true` 以加密通信，设置为 `false` 则不加密。
请注意，如果您将其设置为 `true`，则必须为加密生成密钥和证书
文件。例如，可以使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项：`certfile`

用于 SSL 的证书文件。如果此文件不存在，附加组件启动将失败。

**注意**：文件必须存储在 `/ssl/`，这是 Home Assistant 的默认路径。

### 选项：`keyfile`

用于 SSL 的私钥文件。如果此文件不存在，附加组件启动将失败。

**注意**：文件必须存储在 `/ssl/`，这是 Home Assistant 的默认路径。

### 选项：`leave_front_door_open`

在附加组件配置中添加此选项可通过将其设置为 `true` 来禁用
身份验证。

### 选项：`relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以在现有的 Web 代理中集成
例如在 NGINX 下的相对 URL。默认为 `/`。

### 选项：`status_use_ping`

默认情况下，仪表板使用 mDNS 来检查节点是否在线。如果不是
跨子网工作，除非您的路由器支持 mDNS 转发或 avahi。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求来获取节点状态。如果所有节点在连接时总是显示离线状态，请使用此设置。

### 选项：`streamer_mode`

如果设置为 `true`，这将启用流媒体模式，使 ESPHome 隐藏所有
潜在的私人信息。例如，WiFi (B)SSID（可能用于查找您的位置）、用户名等。请注意，您需要在 YAML 文件中使用
`!secret` 标签，以防止这些信息在编辑和验证时显示。