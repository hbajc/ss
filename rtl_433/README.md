# rtl_433 Home Assistant 附加组件

## 关于

这个附加组件是一个简单的封装，围绕着优秀的 [rtl_433](https://github.com/merbanan/rtl_433) 项目，它通过 [一种支持的 SDR 适配器](https://triq.org/rtl_433/HARDWARE.html) 接收无线传感器数据，解码并以多种格式输出，包括 JSON 和 MQTT。rtl_433 理解的无线传感器主要在 433.92 MHz、868 MHz、315 MHz、345 MHz 和 915 MHz ISM 频段上发送数据。

[查看 rtl_433 文档](https://triq.org/rtl_433)

## 工作原理

这个附加组件所做的就是在 Home Assistant 操作系统管理器下运行 rtl_433。你需要做的就是提供一个配置文件。

默认情况下，rtl_433 会将接收到的数据打印到终端 - 由你来配置它将数据发布到 MQTT，以便 Home Assistant 可以访问它，这可以通过在配置文件中添加一行来完成。

一旦你将 rtl_433 传感器数据引入 MQTT，你需要帮助 Home Assistant 发现并理解这些数据。你可以通过多种方式做到这一点：

  * 在 HA 中手动配置 `sensors` 和 `binary_sensors`，并 [将它们链接到 rtl_433 输出的适当 MQTT 主题](https://www.home-assistant.io/integrations/sensor.mqtt/)，
  * 手动或定期运行 [rtl_433_mqtt_hass.py](https://github.com/merbanan/rtl_433/tree/master/examples/rtl_433_mqtt_hass.py) 脚本，以自动完成大部分配置，或者
  * 安装 [rtl_433 MQTT 自动发现 Home Assistant 附加组件](https://github.com/pbkhrv/rtl_433-hass-addons/tree/main/rtl_433_mqtt_autodiscovery)，这个组件为你运行 rtl_433_mqtt_hass.py。

## 先决条件

要使用这个附加组件，你需要以下内容：

 1. [一个支持 rtl_433 的 SDR 适配器](https://triq.org/rtl_433/HARDWARE.html)。

 2. 在插入 SDR 适配器的机器上运行的 Home Assistant 操作系统。

 3. 一些受 rtl_433 支持的无线传感器。完整的支持协议和设备列表可以在 [rtl_433 的 README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的 "支持设备协议" 部分找到。

## 安装

 1. 创建一个 rtl_433 配置文件，以满足你的需要。如果你在运行 Home Assistant 操作系统的计算机以外的计算机上进行操作，可能会更好，这样你可以自由地进行实验和迭代，直到得到一个有效的配置。请见下文以获取更多细节。

 2. 使用适合你的任何方法（通过 Samba 附加组件、ssh/scp、文件编辑器附加组件等）将配置文件上传到 Home Assistant 的 "/config" 目录。

 3. 安装附加组件。

 5. 将你的 SDR 适配器插入运行附加组件的机器。

 5. 启动附加组件。默认配置将被创建在 `/config/rtl_433/`。要添加或编辑其他配置，请在该目录中创建多个 `.conf.template` 文件。

 6. 启动附加组件并检查日志。

## 配置

对于 "零配置" 设置，安装 [Mosquitto 代理](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md) 附加组件。虽然其他代理可能有效，但未经过测试，并且需要手动配置。一旦安装了该附加组件，启动或重启 rtl_433 和 rtl_433_mqtt_autodiscovery 附加组件，以开始捕获已知的 433 MHz 协议。

对于更高级的配置，请查看 rtl_433 源代码中包含的示例配置文件：[rtl_433.example.conf](https://github.com/merbanan/rtl_433/blob/master/conf/rtl_433.example.conf)

请注意，由于配置文件中有 bash 变量，**美元符号和其他特殊的 shell 字符需要进行转义**。例如，要在配置文件中使用字面字符串 `$GPRMC`，请使用 `\$GPRMC`。

`retain` 选项控制 MQTT 的 `retain` 标志是否默认启用或禁用。可以通过在 `output` 设置中将 `retain` 设置为 `true` 或 `false` 在每个无线电基础上进行覆盖。

在手动配置时，假设你打算将 rtl_433 数据引入 Home Assistant，配置文件中需指定的绝对最小内容是 [MQTT 连接和身份验证信息](https://triq.org/rtl_433/OPERATION.html#mqtt-output)：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY
```

rtl_433 默认监听 433.92MHz，但即使这是你所需的，明确指定频率也是一个好主意，以避免混淆：

```
frequency   433.92M
```

你可能还想缩小 rtl_433 应该尝试解码的协议列表。完整列表可以在 [README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的 "支持设备协议" 部分找到。假设你想实时监听 Acurite 592TXR 温湿度传感器：

```
protocol    40
```

最后但并非最不重要的是，如果你决定使用 MQTT 自动发现脚本或附加组件，其文档建议将 rtl_433 输出的所有数据中的单位转换为 SI：

```
convert     si
```

假设你只有一个 USB 适配器连接，并且 rtl_433 能够自动找到它，最终得到的最小 rtl_433 配置文件如下所示：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY

frequency   433.92M
protocol    40

convert     si
```

请查阅 [官方 rtl_433 文档](https://triq.org/rtl_433) 和 [配置文件示例](https://github.com/merbanan/rtl_433/tree/master/conf) 以获取更多信息。

## 感谢

这个附加组件基于 James Fry 的 [rtl4332mqtt Hass.IO 附加组件](https://github.com/james-fry/hassio-addons/tree/master/rtl4332mqtt)，而这个组件又基于 Chris Kacerguis 的项目：[https://github.com/chriskacerguis/honeywell2mqtt](https://github.com/chriskacerguis/honeywell2mqtt)，而该项目又是基于 Marco Verleun 的 rtl2mqtt 镜像：[https://github.com/roflmao/rtl2mqtt](https://github.com/roflmao/rtl2mqtt)。