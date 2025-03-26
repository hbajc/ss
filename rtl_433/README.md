# rtl_433 Home Assistant 插件

## 关于

这个插件是一个简单的包装器，围绕着优秀的 [rtl_433](https://github.com/merbanan/rtl_433) 项目，它可以通过 [支持的SDR USB加密狗之一](https://triq.org/rtl_433/HARDWARE.html) 接收无线传感器数据，解码并以多种格式输出，包括 JSON 和 MQTT。rtl_433 理解的无线传感器大多数传输数据频率在433.92 MHz、868 MHz、315 MHz、345 MHz和915 MHz ISM频段。

[查看rtl_433文档](https://triq.org/rtl_433)

## 工作原理

这个插件所做的就是在 Home Assistant OS 监督下运行 rtl_433。你需要做的只是提供一个配置文件。

默认情况下，rtl_433 会将接收到的数据打印到终端 - 你需要配置它以将数据发布到 MQTT，以便 Home Assistant 可以访问，这可以通过在配置文件中添加一行来完成。

一旦你将 rtl_433 传感器数据导入到 MQTT，你需要帮助 Home Assistant 发现和理解这些数据。你可以通过多种方式做到这一点：

  * 手动配置 HA 中的 `sensors` 和 `binary_sensors` 并 [将它们链接到从 rtl_433 发出的相应 MQTT 主题](https://www.home-assistant.io/integrations/sensor.mqtt/)，
  * 手动运行 [rtl_433_mqtt_hass.py](https://github.com/merbanan/rtl_433/tree/master/examples/rtl_433_mqtt_hass.py) 脚本，或定时运行，以自动完成大部分配置，或者
  * 安装 [rtl_433 MQTT 自动发现 Home Assistant 插件](https://github.com/pbkhrv/rtl_433-hass-addons/tree/main/rtl_433_mqtt_autodiscovery)，该插件为您运行 rtl_433_mqtt_hass.py。

## 先决条件

使用此插件，你需要以下内容：

 1. [一个支持rtl_433的SDR USB加密狗](https://triq.org/rtl_433/HARDWARE.html)。

 2. 在一台机器上运行 Home Assistant OS，并且SDR USB加密狗已插入。

 3. 一些支持 rtl_433 的无线传感器。支持的协议和设备的完整列表可以在 [rtl_433的README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的“支持的设备协议”部分找到。

## 安装

 1. 创建一个 rtl_433 配置文件，以满足您的需求。如果您在运行 Home Assistant OS 的计算机以外的其他计算机上执行此操作，可能会更好，这样您可以自由实验并迭代，直到找到有效的配置。请查看下面的详细信息。

 2. 通过您能找到的任何方法（通过 Samba 插件、ssh/scp、文件编辑器插件等）将配置文件上传到 Home Assistant 的 "/config" 目录。

 3. 安装插件。

 5. 将您的 SDR USB加密狗插入运行插件的机器。

 5. 启动插件。将默认配置创建在 `/config/rtl_433/` 下。要添加或编辑其他配置，请在该目录中创建多个 `.conf.template` 文件。

 6. 启动插件并检查日志。

## 配置

对于 "零配置" 设置，请安装 [Mosquitto 代理](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md) 插件。虽然其他代理可能有效，但未经过测试并且需要手动设置。一旦插件安装完成，启动或重启 rtl_433 和 rtl_433_mqtt_autodiscovery 插件以开始捕获已知的 433 MHz 协议。

对于更高级的配置，请查看 rtl_433 源代码中包含的示例配置文件：[rtl_433.example.conf](https://github.com/merbanan/rtl_433/blob/master/conf/rtl_433.example.conf)

请注意，由于配置文件中包含了 bash 变量，**美元符号和其他特殊的 shell 字符需要转义**。例如，要在配置文件中使用字面字符串 `$GPRMC`，请使用 `\$GPRMC`。

`retain` 选项控制 MQTT 的 `retain` 标志默认情况下是启用还是禁用。可以通过在 `output` 设置中将 `retain` 设置为 `true` 或 `false` 来逐个无线电覆盖。

在手动配置时，假设您打算将 rtl_433 数据导入 Home Assistant，您在配置文件中需要指定的绝对最小内容是 [MQTT 连接和身份验证信息](https://triq.org/rtl_433/OPERATION.html#mqtt-output)：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY
```

rtl_433 默认监听 433.92MHz，但即使这就是您需要的，明确指定频率可能也是个好主意，以避免混淆：

```
frequency   433.92M
```

您可能还希望缩小 rtl_433 应该尝试解码的协议列表。完整列表可以在 [README](https://github.com/merbanan/rtl_433/blob/master/README.md) 的“支持的设备协议”部分找到。假设您想监听 Acurite 592TXR 温度/湿度传感器：

```
protocol    40
```

最后但并非最不重要的是，如果您决定使用 MQTT 自动发现脚本或插件，其文档建议将所有来自 rtl_433 的数据中的单位转换为 SI：

```
convert     si
```

假设您仅连接了一个 USB 加密狗，并且 rtl_433 能够自动找到它，我们得到了一个最小的 rtl_433 配置文件，如下所示：

```
output      mqtt://HOST:PORT,user=XXXX,pass=YYYYYYY

frequency   433.92M
protocol    40

convert     si
```

更多信息请参阅 [官方 rtl_433 文档](https://triq.org/rtl_433) 和 [配置文件示例](https://github.com/merbanan/rtl_433/tree/master/conf)。

## 贡献

这个插件是基于 James Fry 的 [rtl4332mqtt Hass.IO 插件](https://github.com/james-fry/hassio-addons/tree/master/rtl4332mqtt) 的，而这个插件又是基于 Chris Kacerguis 的项目：[https://github.com/chriskacerguis/honeywell2mqtt](https://github.com/chriskacerguis/honeywell2mqtt)，而这个项目又是基于 Marco Verleun 的 rtl2mqtt 镜像：[https://github.com/roflmao/rtl2mqtt](https://github.com/roflmao/rtl2mqtt)。