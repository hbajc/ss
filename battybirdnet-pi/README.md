# 家庭助理插件: battybirdnet-pi

[![Donate][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![Donate][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbattybirdnet-pi%2Fconfig.json)
![Ingress](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbattybirdnet-pi%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fbattybirdnet-pi%2Fconfig.json)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20(no%20paypal)-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/Buy%20me%20a%20coffee%20with%20Paypal-0070BA?logo=paypal&style=flat&logoColor=white

_感谢所有给我的仓库点星的人！要点星，请点击下面的图片，然后它会在右上角。谢谢！_

[![Stargazers repo roster for @alexbelgium/hassio-addons](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载演变](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/BirdNET-Pi/stats.png)

## 介绍

---

[battybirdnet-pi](https://github.com/rdz-oss/BattyBirdNET-Pi) 是一个实时的声学蝙蝠和鸟类分类系统，基于 BattyBirdNET-Analyzer，适用于 Raspberry Pi 4/5。

插件的特点：
- 提供强大的基础镜像，由 [linuxserver](https://github.com/linuxserver/docker-baseimage-debian) 提供
- 感谢 https://github.com/gdraheim/docker-systemctl-replacement, 工作的 docker 系统
- 使用 HA pulseaudio 服务器
- 使用 HA tmpfs 在内存中存储临时文件，避免磁盘磨损
- 将所有配置文件暴露到 /config，以便于持久存储和方便访问
- 允许修改存储鸟鸣的地点（最好是外接硬盘）
- 支持 ingress，允许安全的远程访问而不暴露端口

## 配置

---

安装插件后，第一次启动插件
可以通过两种方式找到 Webui：
- 通过 HA 的 Ingress（没有密码，但某些功能无法使用）
- 直接访问 <http://homeassistant:port>, 端口为在 birdnet.conf 中定义的端口。当询问密码时，用户名为 `birdnet`，密码为您可以在 birdnet.conf 中定义的密码（默认为空）。这与插件选项中的密码不同，插件选项中的密码是用于访问网页终端的密码

网页终端访问：用户名 `pi`，密码：如插件选项中定义的

您需要一个麦克风：可以使用连接到 HA 的麦克风或 rstp 摄像机的音频流。

可以通过三种方式配置选项：

- 插件选项

```yaml
BIRDSONGS_FOLDER: 存储鸟歌曲文件的文件夹 # 如果您想避免分析阻塞，应该使用 SSD
MQTT_DISABLED : 如果为 true，则禁用自动 mqtt 发布。只有在已经有本地代理时才有效
LIVESTREAM_BOOT_ENABLED: 从启动时开始直播，或从设置中开始
PROCESSED_FOLDER_ENABLED : 如果启用，您需要在 birdnet.conf（或 birdnet 的设置）中设置将在 tmpfs 内的临时文件夹 "/tmp/Processed" 中保存的最后 wav 文件数量（以避免磁盘磨损），如果您想检索它们。这个数量可以通过插件选项进行调整
TZ: Etc/UTC 指定要使用的时区，请参见 https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List
pi_password: 设置访问网页终端的用户密码
localdisks: sda1 #将要挂载的驱动器的硬件名称（CSV分隔），或其标签写在这里。例如 sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，要挂载的 smb 服务器列表，以逗号分隔
cifsusername: "username" # 可选，所有 smb 共享的 smb 用户名
cifspassword: "password" # 可选，smb 密码
cifsdomain: "domain" # 可选，允许设置 smb 共享的域
```

- Config.yaml
额外的变量可以通过在 /config/db21ed7f_battybirdnet-pi/config.yaml 中找到的 config.yaml 文件进行配置，使用 Filebrowser 插件

- Config_env.yaml
额外的环境变量可以在这里配置

## 安装

---

安装此插件相当简单，跟安装其他插件没有区别。

1. 将我的插件库添加到您的家庭助理实例（在主管插件商店右上角，或者如果您已经配置了我的 HA，请点击下面的按钮）
   [![打开您的 Home Assistant 实例，并显示添加插件仓库对话框，带有预填充的特定仓库 URL。](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons)
1. 安装此插件。
1. 点击 `保存` 按钮以存储您的配置。
1. 根据您的喜好设置插件选项
1. 启动插件。
1. 检查插件的日志，以查看是否一切正常。
1. 打开 WebUI，并调整软件选项

## 与 HA 的集成

---
### Apprise

您可以使用 Apprise 通过 mqtt 发送通知，然后使用 HomeAssistant 对其进行操作
更多信息请参考： https://wander.ingstar.com/projects/birdnetpi.html

### 自动 mqtt

如果安装了 mqtt，插件会在每次检测到物种时自动更新 birdnet 主题

## 使用 ssl

---

选项 1：安装 Let's Encrypt 插件，生成证书。它们默认为存储在 /ssl 中的 certfile.pem 和 keyfile.pem。只需从插件选项启用 ssl，就可以工作。

选项 2：启用 80 端口，将您的 battybirdnet-pi URL 定义为 https。证书将由 Caddy 自动生成

## 改善检测

---

### 声卡增益

在终端标签页使用 alsamixer，确保音量水平足够高但不过高（不要进入红色部分）
https://github.com/mcguirepr89/BirdNET-Pi/wiki/Adjusting-your-sound-card

### 铁氧体

在我的案例中，添加铁氧体珠会导致更糟的噪音

### 耳机转 USB 适配器

根据我的测试，只有使用 KT0210（如 Ugreen 的）适配器有效。我无法让基于 ALC 的适配器被检测到。

### 麦克风比较

推荐麦克风（[完整讨论在这里](https://github.com/mcguirepr89/BirdNET-Pi/discussions/39)）：
- Clippy EM272 (https://www.veldshop.nl/en/smart-clippy-em272z1-mono-omni-microphone.html) + ugreen 耳机转 USB 连接器：最佳灵敏度，配有领夹麦克风技术
- Boya By-LM40：最佳质量/价格比
- Hyperx Quadcast：最佳灵敏度，配有心形指向性技术

结论，使用 Dahua 的麦克风就足够了，EM272 是最佳选择，但 Boya By-LM40 是一个非常好的折中，因为 birndet 模型分析的频率范围是 0-15000Hz

![image](https://github.com/alexbelgium/hassio-addons/assets/44178713/df992b79-7171-4f73-b0c0-55eb4256cd5b)

### 降噪 ([完整讨论在这里](https://github.com/mcguirepr89/BirdNET-Pi/discussions/597))

降噪在严肃研究者中不被看好。然而，它似乎显著提高了检测质量！以下是在 HA 中如何做到这一点：
- 使用 Portainer 插件，进入 hassio_audio 容器，并修改文件 /etc/pulse/system.pa，添加行 `load-module module-echo-cancel`
- 进入 Terminal 插件，输入 `ha audio restart`
- 在插件选项中选择降噪设备作为输入设备

### 高通滤波

应避免使用，因为模型使用整个 0-15khz 范围

## 常见问题

尚不可用

## 支持

在 GitHub 上创建一个问题

---