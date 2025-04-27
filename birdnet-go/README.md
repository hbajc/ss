## &#9888; 打开的问题 : [🐛 [Birdnet-go] 在重启时音频设置被覆盖 (打开于 2025-02-21)](https://github.com/alexbelgium/hassio-addons/issues/1781) 由 [@Lotwook](https://github.com/Lotwook)
## &#9888; 打开的问题 : [🐛 [Birdnet-go] USB 麦克风在 UI 中可选择，但不工作 (打开于 2025-03-12)](https://github.com/alexbelgium/hassio-addons/issues/1808) 由 [@melor](https://github.com/melor)
# Home Assistant 插件：Birdnet-Go

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-go%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-go%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbirdnet-go%2Fconfig.json)

[![Codacy 徽章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢每一个给我的仓库加星的人！如果要加星，请点击下面的图片，然后它会在右上角。谢谢！_

[![@alexbelgium/hassio-addons 的 Stargazers 仓库名单](https://reporoster.com/stars/alexbelgium/hassio-addons)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/birdnet-go/stats.png)

## 关于

[BirdNET-Go](https://github.com/tphakala/birdnet-go/tree/main) 是一项用于连续鸟类监测和识别的 AI 解决方案，由 @tphakala 开发。

该插件基于他们的 Docker 镜像。

## 配置

安装后，第一次启动插件。WebUI 可以在 <http://homeassistant:8080> 找到。
您需要一个麦克风：可以使用一个连接到 HA 的麦克风或 RTSP 摄像头的音频流。

音频剪辑文件夹可以通过从插件选项挂载于外部或 SMB 驱动器来存储，然后指定路径而不是 "clips/"。例如，"/mnt/NAS/Birdnet/"

可以通过三种方式配置选项：

- 插件选项

```yaml
ALSA_CARD : 卡号（通常为 0 或 1），请参阅 https://github.com/tphakala/birdnet-go/blob/main/doc/installation.md#deciding-alsa_card-value
TZ: Etc/UTC 指定要使用的时区，请参阅 https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
COMMAND : realtime --rtsp url # 允许提供参数给 birdnet-go
```

- Config.yaml
可以使用在 /config/db21ed7f_birdnet-go/config.yaml 中找到的 config.yaml 文件配置其他变量，使用 Filebrowser 插件。

- Config_env.yaml
可以在那里配置其他环境变量。

## 安装

安装此插件非常简单，与安装其他任何插件没有区别。

1. 将我的插件仓库添加到您的 Home Assistant 实例中（在管理面板的插件商店右上角，或者如果您已配置我的 HA，请单击下面的按钮）

   [![打开您的 Home Assistant 实例并显示添加插件仓库对话框，预填充特定的仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
2. 安装此插件。
3. 点击 `保存` 按钮以保存您的配置。
4. 根据您的偏好设置插件选项。
5. 启动插件。
6. 检查插件的日志，以查看是否一切正常。
7. 打开 webUI 并调整软件选项。

## 与 HA 集成

Home Assistant 集成说明在这里找到，[Birdnet-Go 插件：Home Assistant 集成](./HAINTEGRATION.md)

## 使用 VLC 设置 RTSP 源

VLC 打开一个 TCP 端口，但流是 UDP 的。为此，需要配置 Birdnet-Go 使用 UDP。将 config.yaml 文件调整为 UDP 或使用 birdnet-go 命令行选项：

`--rtsptransport udp --rtsp rtsp://192.168.1.21:8080/stream.sdp`

### Linux 指令

使用以下命令之一在没有界面的情况下运行 vlc：

```bash
# 对大多数设备来说，这应该有效
/usr/bin/vlc -I dummy -vvv alsa://hw:0,0 --no-sout-all --sout-keep --sout '#transcode{acodec=mpga}:rtp{sdp=rtsp://:8080/stream.sdp}'

# 如果第一个命令无效，请尝试这个
/usr/bin/vlc -I dummy -vvv alsa://hw:4,0 --no-sout-all --sout-keep --sout '#rtp{sdp=rtsp://:8080/stream.sdp}'
```

运行 `arecord -l` 获取麦克风硬件信息：

```text
**** 捕获硬件设备列表 ****
卡 0: PCH [HDA Intel PCH], 设备 0: ALC3220 模拟 [ALC3220 Analog]
  次设备: 1/1
  次设备 #0: 次设备 #0
卡 2: S7 [SteelSeries Arctis 7], 设备 0: USB 音频 [USB Audio]
  次设备: 1/1
  次设备 #0: 次设备 #0
卡 3: Nano [Yeti Nano], 设备 0: USB 音频 [USB Audio]
  次设备: 1/1
  次设备 #0: 次设备 #0
卡 4: 设备 [USB PnP 声音设备], 设备 0: USB 音频 [USB Audio]
  次设备: 0/1
  次设备 #0: 次设备 #0
```

hw:4,0 = **卡 4**: 设备 [USB PnP 声音设备], **设备 0**: USB 音频 [USB Audio]

Systemd 服务文件示例。相应地调整 user:group。如果您希望以 root 身份运行，则可能需要运行 vlc-wrapper 而不是 vlc。

```text
[Unit]
Description=VLC Birdnet RTSP 服务器
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
StandardOutput=journal
ExecStart=/usr/bin/vlc -I dummy -vvv alsa://hw:0,0 --sout '#transcode{acodec=mpga}:rtp{sdp=rtsp://:8080/stream.sdp}'
User=someone
Group=somegroup

[Install]
WantedBy=multi-user.target
```

## 常见问题

尚未提供

## 支持

在 GitHub 上创建一个问题

---

![插图](https://raw.githubusercontent.com/tphakala/birdnet-go/main/doc/BirdNET-Go-dashboard.webp)