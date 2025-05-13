# Home Assistant 插件：Z-Wave JS

## 安装

按照以下步骤在您的系统上安装插件：

1. 在 Home Assistant 前端导航到 **设置** -> **插件** -> **插件商店**。
2. 找到 "Z-Wave JS" 插件并点击它。
3. 点击 "安装" 按钮。

## 如何使用

插件需要知道您的 Z-Wave 设备的插头位置，因此，您需要配置插件以指向正确的设备。

如果您正在使用 Home Assistant，可以通过访问 `设置 -> 系统 -> 硬件` 找到此值，然后点击三个点的菜单并选择 `所有硬件`。建议使用 "by-id" 路径指向设备（如果存在），因为它在添加其他设备后不会改变。

1. 在插件配置中的 `device` 选项中替换 `null` 并在引号中指定设备名称：例如，类似于 `"/dev/serial/by-id/usb-0658_0200-if00"`、`"/dev/ttyUSB0"`、`"/dev/ttyAMA0"` 或 `"/dev/ttyACM0"`。
2. 以 `2232666D1...` 的形式设置您的 16 字节（32 个字符的十六进制）安全密钥，以安全连接到兼容设备。建议配置所有四个网络密钥，因为某些启用安全的设备（锁等）如果不安全添加可能无法正常工作。
   - 需要注意的是，建议不要安全连接 _所有_ 设备，除非它们支持 S2 安全性，因为 S0 安全会使网络中发送的消息数量增加三倍。
3. 点击 "保存" 以保存插件配置。
4. 启动插件。
5. 将 Z-Wave JS 集成添加到 Home Assistant，参见文档：<https://www.home-assistant.io/integrations/zwave_js>

## 配置

插件配置：

```yaml
device: /dev/ttyUSB0
s0_legacy_key: 2232666D100F795E5BB17F0A1BB7A146
s2_access_control_key: A97D2A51A6D4022998BEFC7B5DAE8EA1
s2_authenticated_key: 309D4AAEF63EFD85967D76ECA014D1DF
s2_unauthenticated_key: CF338FE0CB99549F7C0EA96308E5A403
lr_s2_access_control_key: E2CEA6B5986C818EEC0D0065D81E2BD5
lr_s2_authenticated_key: 863027C59CFC522A9A3C41976AE54254
```

### 选项 `device`

Z-Wave 控制器设备。

如果您正在使用 Home Assistant，可以通过访问 `设置 -> 系统 -> 硬件` 找到此值，然后点击三个点的菜单并选择 `所有硬件`。建议使用 "by-id" 路径指向设备（如果存在），因为它在添加其他设备后不会改变。

在大多数情况下，它看起来像以下其中之一：

- `"/dev/serial/by-id/usb-0658_0200-if00"`
- `"/dev/ttyUSB0"`
- `"/dev/ttyAMA0"`
- `"/dev/ttyACM0"`

### 安全密钥

需要六个不同的安全密钥，以充分利用 Z-Wave JS 支持的不同设备加入方法：`s0_legacy_key`、`s2_access_control_key`、`s2_authenticated_key`、`s2_unauthenticated_key`、`lr_s2_access_control_key` 和 `lr_s2_authenticated_key`。

如果您是从之前版本的 `zwave-js` 过来的，您的密钥可能存储在 `network_key` 配置选项中。当插件首次启动时，密钥将从 `network_key` 迁移到 `s0_legacy_key`，这将确保您的 S0 安全设备继续正常工作。

如果启动时缺少任何这些密钥，插件会为您自动生成一个。要手动生成网络密钥，您可以在 SSH 插件中使用以下脚本：

```bash
hexdump -n 16 -e '4/4 "%08X" 1 "\n"' /dev/random
```

您也可以使用此类网站生成所需的数据：

<https://www.random.org/cgi-bin/randbyte?nbytes=16&format=h>

请确保备份这些密钥。如果需要重建系统而没有这些密钥的备份，您将无法与任何安全加入的设备通信。这可能意味着您必须对这些设备和您的控制器进行工厂重置，然后重新建立您的 Z-Wave 网络。

> 注意：在多个安全类之间共享密钥是一个安全风险，因此如果您选择自行配置这些密钥，请确保使其唯一！

#### 选项 `s0_legacy_key`

S0 安全 Z-Wave 设备在加入网络之前需要一个网络密钥。此配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的。

#### 选项 `s2_access_control_key`

必须提供 `s2_access_control_key` 以便包含具有 S2 访问控制安全类的设备。此安全类是门锁和车库门开启器等设备所需的。此配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的。

#### 选项 `s2_authenticated_key`

必须提供 `s2_authenticated_key` 以便包含具有 S2 认证安全类的设备。安保系统、传感器、照明等设备可以请求此安全类。此配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的。

### 选项 `s2_unauthenticated_key`

必须提供 `s2_unauthenticated_key` 以便包含具有 S2 未认证安全类的设备。这与 S2 认证类似，但不验证包含的设备是否正确。此配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的。

#### 选项 `lr_s2_access_control_key`

必须提供 `lr_s2_access_control_key` 以便包含使用 Z-Wave 长距离的设备。此配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的。

#### 选项 `lr_s2_authenticated_key`

必须提供 `lr_s2_authenticated_key` 以便包含使用 Z-Wave 长距离的设备。此配置选项是必需的，但如果未设置，插件将在启动时自动生成一个新的。

### 选项 `log_level`（可选）

此选项设置 Z-Wave JS 的日志级别。有效选项包括：

- silly
- debug
- verbose
- http
- info
- warn
- error

如果没有指定 `log_level`，日志级别将设置为在 Supervisor 中设置的级别。

### 选项 `log_to_file`（可选）

当启用此选项时，日志将写入 `/addon_configs/core_zwave_js` 文件夹，文件扩展名为 `.log`。

### 选项 `log_max_files`（可选）

当 `log_to_file` 为真时，Z-Wave JS 将为每一天创建一个日志文件。此选项允许您控制 Z-Wave JS 将保留的最大文件数量。

### 选项 `soft_reset`（可选）

此设置告诉插件如何处理 500 系列控制器的软重置：
1. 自动 - 插件将决定是否为 500 系列控制器启用或禁用软重置。这是默认选项，适合大多数人。
2. 启用 - 将显式为 500 系列控制器启用软重置。
3. 禁用 - 将显式为 500 系列控制器禁用软重置。

### 选项 `emulate_hardware`（可选）

如果您没有 USB 插头，可以使用伪装的插头进行测试。
它将无法控制任何实际设备。

### 选项 `disable_controller_recovery`（可选）：

此设置将禁用 Z-Wave JS 在控制器似乎无反应时的自动恢复过程，而是让控制器自行恢复（如果能恢复的话）。当控制器无响应时，命令将开始失败，节点可能会随机标记为死节点。如果控制器无法自行恢复，您需要重启插件以尝试恢复。在大多数情况下，用户将不需要使用此功能，因此仅在您知道自己在做什么和/或被要求时才更改此设置。

### 选项 `disable_watchdog`（可选）：

此设置将阻止 Z-Wave JS 在支持的控制器上启用硬件看门狗。在大多数情况下，用户将不需要使用此功能，因此仅在您知道自己在做什么和/或被要求时才更改此设置。

### 选项 `safe_mode`（可选）

此设置将您的网络置于安全模式，这可能会显著降低网络性能，但也可能有助于使网络正常运行，以便您可以排除故障、获取日志等。在大多数情况下，用户将不需要使用此功能，因此仅在您知道自己在做什么和/或被要求时才更改此设置。

### 选项 `network_key`（已弃用）

在插件的早期版本中，这是唯一需要的密钥。随着在 zwave-js 中引入 S2 安全性加入，已弃用此选项，取而代之的是 `s0_legacy_key`。如果仍然设置，`network_key` 的值将在第一次启动时迁移到 `s0_legacy_key`。

### 排除网络问题

此插件中提供了几个功能，以帮助您排除网络问题和/或提供数据给 Home Assistant 或 Z-Wave JS 团队，以帮助追踪问题：

1. **更新日志级别**：在打开 GitHub 问题时，将 `log_level` 配置选项设置为 `debug` 并捕捉问题发生时的数据非常有用。
2. **记录到文件**：`log_to_file` 和 `log_max_files` 配置选项允许您启用和配置该功能。请注意，要访问日志文件，您需要能够访问 HA 实例的文件系统，您可以通过文件编辑器、samba、ssh 插件等方式进行访问。
3. **访问 Z-Wave JS 缓存**：Z-Wave JS 将其发现的网络信息存储在缓存文件中，以免在每次启动时重新采访设备。在某些情况下，在打开 GitHub 问题时，可能会要求您提供缓存文件。您可以在 `/addon_configs/core_zwave_js/cache` 中访问它们。请注意，要访问缓存，您需要能够访问 HA 实例的文件系统，您可以通过文件编辑器、samba、ssh 插件等方式进行访问。
4. **更改软重置行为**：默认情况下，插件将选择是否在启动时自动软重置控制器。在大多数情况下不应更改，但如果在排除问题时被要求进行更改，您可以通过 `soft_reset` 配置选项进行更改。
5. **禁用控制器恢复**：默认情况下，如果网络控制器似乎被卡住，Z-Wave JS 将自动尝试恢复控制器到健康状态。在大多数情况下不应更改，但如果在排除问题时被要求进行更改，您可以通过 `disable_controller_recovery` 配置选项进行更改。
6. **启用安全模式**：当 Z-Wave JS 启动时遇到困难时，获取有用的日志进行排除问题可能非常困难。通过将 `safe_mode` 设置为 true，Z-Wave JS 可能能够在设置为 false 的情况下启动。请注意，启用 `safe_mode` 将对网络性能产生负面影响，应谨慎使用。

## 已知问题和限制

- 您的硬件需要与 Z-Wave JS 库兼容。

## 支持

有问题吗？

您有几种选项可以获取答案：

- [Home Assistant Discord 聊天服务器][discord]。
- Home Assistant [社区论坛][forum]。
- 加入 [Reddit 论坛][reddit] 在 [/r/homeassistant][reddit]。

如果您发现了一个错误，请 [在我们的 GitHub 上提出问题][issue]。

[discord]: https://discord.gg/c5DvZ4e
[forum]: https://community.home-assistant.io
[issue]: https://github.com/home-assistant/addons/issues
[reddit]: https://reddit.com/r/homeassistant