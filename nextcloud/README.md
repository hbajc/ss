## &#9888; 开放请求 : [✨ [请求] immich 和 Nextcloud 入口支持 (打开于 2025-03-15)](https://github.com/alexbelgium/hassio-addons/issues/1812) 由 [@bessertristan09](https://github.com/bessertristan09)
## &#9888; 开放问题 : [🐛 [Nextcloud] 无法上传大文件 (打开于 2025-05-15)](https://github.com/alexbelgium/hassio-addons/issues/1866) 由 [@HaltingSleuth42](https://github.com/HaltingSleuth42)
# Home Assistant 插件：Nextcloud

[![捐赠][donation-badge]](https://www.buymeacoffee.com/alexbelgium)
[![捐赠][paypal-badge]](https://www.paypal.com/donate/?hosted_button_id=DZFULJZTP3UQA)

![版本](https://img.shields.io/badge/dynamic/json?label=Version&query=%24.version&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnextcloud%2Fconfig.json)
![入口](https://img.shields.io/badge/dynamic/json?label=Ingress&query=%24.ingress&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnextcloud%2Fconfig.json)
![架构](https://img.shields.io/badge/dynamic/json?color=success&label=Arch&query=%24.arch&url=https%3A%2F%2Fraw.githubusercontent.com%2Falexbelgium%2Fhassio-addons%2Fmaster%2Fnextcloud%2Fconfig.json)

[![Codacy勋章](https://app.codacy.com/project/badge/Grade/9c6cf10bdbba45ecb202d7f579b5be0e)](https://www.codacy.com/gh/alexbelgium/hassio-addons/dashboard?utm_source=github.com&utm_medium=referral&utm_content=alexbelgium/hassio-addons&utm_campaign=Badge_Grade)
[![GitHub Super-Linter](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/weekly-supelinter.yaml?label=Lint%20code%20base)](https://github.com/alexbelgium/hassio-addons/actions/workflows/weekly-supelinter.yaml)
[![构建器](https://img.shields.io/github/actions/workflow/status/alexbelgium/hassio-addons/onpush_builder.yaml?label=Builder)](https://github.com/alexbelgium/hassio-addons/actions/workflows/onpush_builder.yaml)

[donation-badge]: https://img.shields.io/badge/买我一杯咖啡（无paypal）-%23d32f2f?logo=buy-me-a-coffee&style=flat&logoColor=white
[paypal-badge]: https://img.shields.io/badge/用Paypal给我买杯咖啡-0070BA?logo=paypal&style=flat&logoColor=white

![使用elasticsearch][elasticsearch-shield]

_感谢所有在我的仓库上点星的人！要点星，请点击下面的图片，然后它会出现在右上角。谢谢！_

[![星星计数](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/.github/stars2.svg)](https://github.com/alexbelgium/hassio-addons/stargazers)

![下载量变化](https://raw.githubusercontent.com/alexbelgium/hassio-addons/master/nextcloud/stats.png)

## 关于

各种调整和配置选项的添加。
最初的分支来自版本 : https://github.com/haberda/hassio_addons
此插件基于来自 linuxserver.io 的 [docker 镜像](https://github.com/linuxserver/docker-nextcloud)。

## 配置

### 自定义脚本

/config/addons_autoscripts/nextcloud-ocr.sh 将在启动时执行。
要在启动时运行自定义命令，可以尝试以下代码：
```bash
#!/usr/bin/with-contenv bashio
# shellcheck shell=bash

#################
# 代码注入器 #
#################

# 写在此 bash 脚本中的任何命令将在插件启动时执行
# 请查看这里的指南 : https://github.com/alexbelgium/hassio-addons/wiki/Add%E2%80%90ons-feature-:-customisation

# 仅在初始化完成后运行
# shellcheck disable=SC2128
mkdir -p /scripts
if [ ! -f /app/www/public/occ ]; then cp /config/addons_autoscripts/"$(basename "${BASH_SOURCE}")" /scripts/ && exit 0; fi

echo "扫描文件"
sudo -u abc php /app/www/public/occ files:scan --all
echo "完成！"
```

### 插件选项

```yaml
default_phone_region: CN # 根据 https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements 定义默认电话区域
disable_updates: 防止插件自动更新应用程序
additional_apps: vim,nextcloud #指定要安装的其他 apk 文件；用逗号分隔
PGID/PUID: 1000 #允许设置用户。
trusted_domains: your-domain.com #允许选择受信任的域。未在此列表中的域将被删除，除了初始配置中使用的第一个域。
OCR: false #设置为 true 以安装 tesseract-ocr 功能。
OCRLANG: fra,eng #可以从此页面设置任何语言（始终三个字母）[这里](https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016)。
data_directory: 主数据目录的路径。默认为 `/config/data`。仅用于设置权限和预填初始安装模板。初始安装完成后不能更改
enable_thumbnails: true/false # 启用媒体文件的缩略图生成（在旧系统中禁用）
use_own_certs: true/false #如果为 true，使用指定的 certfile 和 keyfile
certfile: fullchain.pem #ssl 证书，必须位于 /ssl 中
keyfile: privkey.pem #ssl 密钥文件，必须位于 /ssl 中
localdisks: sda1 #将要挂载的驱动器的硬件名称用逗号分隔，或其标签。例：sda1, sdb1, MYNAS...
networkdisks: "//SERVER/SHARE" # 可选，列出要挂载的 smbv2/3 服务器，用逗号分隔
cifsusername: "用户名" # 可选，smb 用户名，所有 smb 共享相同
cifspassword: "密码" # 可选，smb 密码，所有 smb 共享相同
env_memory_limit: nextcloud 可用内存限制（默认是 512M）
env_post_max_size: nextcloud post 大小（默认是 512M）
env_upload_max_filesize; nextcloud 上传大小（默认是 512M）
```

Web 界面可以在 `<your-ip>:port` 找到。

### 更改临时文件夹以避免在 HA 系统上占用 eMMC 空间（感谢 @senna1992）

请查看 ; https://github.com/alexbelgium/hassio-addons/discussions/1370

### 使用 mariadb 作为主数据库（感谢 @amaciuc）

如果您在首次运行 `webui` 时看到以下警告：

```bash
性能警告
您选择了 SQLite 作为数据库。
SQLite 应仅用于最小和开发实例。对于生产，我们推荐使用不同的数据库后端。
如果您使用文件同步客户端，强烈不建议使用 SQLite。
```

并且您想克服此问题，请按照以下步骤进行：

- 1. 安装 `mariadb` 插件，使用一些随机信息进行配置并启动它。成功启动它至关重要，以便在网络中被 `nextcloud` 看到。
- 2. 安装 `nextcloud` 插件（或者如果已经安装则重启它），观察日志，直到您注意到以下 `警告`：

  ```bash
  警告： 找到 MariaDB 插件！由于 Nextcloud 的工作方式，它无法自动配置，但您可以在第一次运行网页用户界面时使用这些值手动配置：
  数据库用户 : service
  数据库密码 : Eangohyuchae6aif7saich2nies8xaivaejaNgaev6gi3yohy8ha2aexaetei6oh
  数据库名称 : nextcloud
  主机名 : core-mariadb:3306
  ```

- 3. 返回 `mariadb` 插件，用上述凭据进行配置并重启。确保插件正在创建 `netxcloud` 数据库。
- 4. 进入网页用户界面并填写所有必需信息。您可以在这里查看一个例子：

![image](https://user-images.githubusercontent.com/19391765/207888717-50b43002-a5e2-4782-b5c9-1f582309df2b.png)

## 安装

此插件的安装非常简单，与安装其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击 `保存` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 进入网页用户界面，您将在其中创建用户名、密码和数据库（如果使用 mariadb，信息在日志中）
1. 重启插件，以应用任何需要应用的选项

## HA 集成

查看此组件 : https://www.home-assistant.io/integrations/nextcloud/

[repository]: https://github.com/alexbelgium/hassio-addons
[elasticsearch-shield]: https://img.shields.io/badge/Elasticsearch-optional-blue.svg?logo=elasticsearch