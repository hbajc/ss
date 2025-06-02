# 配对

默认情况下，插件的 `permit_join` 设置为 `false`。要允许设备加入，您需要在插件启动后激活此选项。您现在可以使用 [内置前端](https://www.zigbee2mqtt.io/information/frontend.html) 来实现这一点。有关如何启用内置前端的更多详细信息，请参见下一部分。

# 启用内置前端

启用 `ingress` 以在用户界面中提供前端：**设置 → 插件 → Zigbee2MQTT → 在侧边栏显示**。您可以在 [Zigbee2MQTT 文档](https://www.zigbee2mqtt.io/information/frontend.html) 上找到有关此功能的更多详细信息。

# 配置

## 入门

[入门](https://www.zigbee2mqtt.io/guide/getting-started/#onboarding) 允许您在无需手动输入详细信息的情况下设置 Zigbee2MQTT。当您用全新安装（没有现有配置）启动插件时，前端将显示快速设置页面，允许您选择各种 Zigbee2MQTT 设置以便能够启动。

> [!NOTE]
> 成功检测可供选择的适配器可能会基于您的设置/网络而有所不同。您可能需要在页面上手动输入这些 [详细信息](https://www.zigbee2mqtt.io/guide/configuration/adapter-settings.html#basic-configuration)。

> [!TIP]
> 您可以使用插件配置页面中的切换按钮强制重新运行入门（例如，更换适配器）（在勾选 `显示未使用的可选配置选项` 之后可见）。这将强制入门在您首次成功配置后重新运行。完成后，请确保将其禁用。

## 手动

启动 Zigbee2MQTT 所需的配置可从插件配置中获得。其余选项可以通过 Zigbee2MQTT 前端进行配置。

> [!CAUTION]
> 通过插件配置页面配置的设置将优先于 `configuration.yaml` 页面中的设置（例如，您在插件配置页面中设置 `rtscts: false`，在 `configuration.yaml` 中设置 `rtscts: true`，将使用 `rtscts: false`）。_如果您希望通过 YAML 控制整个配置，请从插件配置页面中移除它们。_

#### 每个配置部分的示例

- socat
  ```yaml
  enabled: false
  master: pty,raw,echo=0,link=/tmp/ttyZ2M,mode=777
  slave: tcp-listen:8485,keepalive,nodelay,reuseaddr,keepidle=1,keepintvl=1,keepcnt=5
  options: "-d -d"
  log: false
  ```
- mqtt
  ```yaml
  server: mqtt://localhost:1883
  user: my_user
  password: "my_password"
  ```
- serial
  ```yaml
  adapter: zstack
  port: /dev/serial/by-id/usb-Texas_Instruments_TI_CC2531_USB_CDC___0X00124B0018ED3DDF-if00
  ```

# 配置备份

插件将在您的数据路径中创建 `configuration.yml` 的备份：`$DATA_PATH/configuration.yaml.bk`。在升级时，您应使用此备份填充新配置中的相关值，特别是网络密钥，以避免破坏网络并需要重新配对所有设备。如果在插件启动时未找到以前的备份，将创建配置的备份。

# 启用看门狗

为了在发生软故障（如“适配器断开”）的情况下自动重启 Zigbee2MQTT，可以使用看门狗。通过将以下内容添加到插件配置中，可以启用它：

```yaml
watchdog: default
```

这将使用默认的看门狗重试延迟为 1 分钟、5 分钟、15 分钟、30 分钟、60 分钟。也支持自定义延迟，例如 `watchdog: 5,10,30` 将以 5 分钟、10 分钟、30 分钟的重试延迟启动 Zigbee2MQTT。有关看门狗的更多信息，请阅读 [文档](https://www.zigbee2mqtt.io/guide/installation/15_watchdog.html)。

# 添加对新设备的支持

如果您有兴趣为 Zigbee2MQTT 添加对新设备的支持，请参见 [如何支持新设备](https://www.zigbee2mqtt.io/how_tos/how_to_support_new_devices.html)。

# 注意事项

- 根据您的配置，MQTT 服务器配置可能需要包含端口，通常是 `1883` 或 `8883` 用于 SSL 通信。例如，`mqtt://core-mosquitto:1883` 适用于 Home Assistant 的 Mosquitto 插件。
- 要找到您暴露的串口，请转到 **主管 → 系统 → 主机系统 → ⋮ → 硬件**

# Socat

在某些情况下，无法将串行设备转发到 Zigbee2mqtt 运行的容器。这可能是因为该设备根本没有物理连接到计算机。

可以使用 Socat 在 TCP 上转发串行设备到 Zigbee2mqtt。有关更多信息，请参见 [socat 手册](https://linux.die.net/man/1/socat)。

您可以在 socat 部分中使用以下选项配置 socat 模块：

- `enabled` true/false 启用 socat（默认：false）
- `master` 在 socat 命令行中使用的主地址或第一个地址（必需）
- `slave` 在 socat 命令行中使用的从地址或第二个地址（必需）
- `options` 添加到 socat 命令行的额外选项（可选）
- `log` true/false 是否将 socat stdout/stderr 日志到 data_path/socat.log（默认：false）

**注意：** 您必须根据需要更改 `master` 和 `slave` 选项。默认值将确保 socat 监听端口 `8485` 并将其输出重定向到 `/dev/ttyZ2M`。Zigbee2mqtt 的串口设置不会自动设置，必须相应更改。