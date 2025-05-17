# Apache2 Webserver Add-on for Home Assistant OS
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]
![项目维护][maintenance-shield]

![Ingress 支持](../_images/apache2/ingress.png)

为 Home Assistant OS 提供的轻量级 Apache2 网页服务器附加组件，支持可选的 PHP 8 和 MariaDB。

此附加组件允许您提供静态或动态网站，运行基于 PHP 的应用程序，或通过网页界面暴露内部服务。提供多种版本以适应不同的需求和用例。

---

## 📋 目录

- [关于](#关于)
- [版本](#版本)
- [安装](#安装)
- [配置](#配置)
- [认证](#认证)
- [Ingress](#ingress)
- [MariaDB 使用](#mariadb-使用)
- [限制](#限制)
- [支持](#支持)
- [许可证](#许可证)

---

## 📖 关于

此附加组件提供 [Apache HTTP Server](https://httpd.apache.org/) 用于 Home Assistant OS。它支持：

- 托管静态 HTML/CSS/JS 网站
- 运行 PHP 应用程序（如仪表板、工具）
- 可选的 MariaDB 集成（如用于 WordPress、phpMyAdmin）

Apache HTTP Server 是由 Apache 软件基金会维护的开源网页服务器软件。

---

## 🧰 版本

| 版本 | 特性 |
|------|------|
| [完整版本](https://github.com/FaserF/hassio-addons/tree/master/apache2) | Apache2、PHP 8.4（附带常用扩展）、MariaDB 客户端、ffmpeg、Mosquitto |
| [最小版本](https://github.com/FaserF/hassio-addons/tree/master/apache2-minimal) | 仅 Apache2 |
| [最小 + MariaDB](https://github.com/FaserF/hassio-addons/tree/master/apache2-minimal-mariadb) | Apache2、MariaDB 客户端、附带基本模块的 PHP |

---

## 🚀 安装

1. 将仓库添加到 Home Assistant:
   [![添加仓库](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)

2. 通过 Supervisor 安装 `Apache2` 附加组件。

3. 将您的网站文件放置在 document_root 中（默认：`/share/htdocs`）。
   示例：`/share/htdocs/index.html`

4. 启动附加组件并通过 Ingress 或外部端口访问您的网站。

---

## ⚙️ 配置

```yaml
document_root: /share/htdocs               # 必填项
php_ini: default                           # "default"、"get_file" 或路径
default_conf: default                      # Apache 默认配置
default_ssl_conf: default                  # Apache SSL 配置
website_name: mydomain.local               # 如果 ssl 为 true 则必填
username: apache                           # 可选，修改文件所有权
password: mySecretPassword                 # 可选，用于内部文件访问
ssl: true                                  # 启用 HTTPS
certfile: fullchain.pem                    # 如果 ssl 为 true 则必填
keyfile: privkey.pem                       # 如果 ssl 为 true 则必填
init_commands:                             # 可选启动命令
  - apk add imagemagick
```

您可以使用 `get_file` 从 `/share` 提取自己的配置文件和 PHP.ini。

### 选项: `document_root`

此选项是必需的。根据您在 Home Assistant 安装中的根网页文件夹位置进行更改。

注意：必须位于 /share 或 /media 文件夹中！其他文件夹对该附加组件不可见。

### 选项: `php_ini`

您可以选择以下选项：

default → 使用内置的 PHP 8.4 配置文件（推荐）

get_file → 将默认 PHP 8.4 `php.ini` 复制到 `/share/apache2addon_php.ini`

path/to/your/new/php.ini -> 请根据您的自定义 php.ini 文件的位置更改路径，如：/share/apache2/php.ini

### 选项: `default_conf` & `default_ssl_conf`

您可以选择以下选项：

default -> 使用默认的 apache2 附加组件文件

get_config -> 将默认 apache2 附加组件配置文件的副本获取到您的 /share 文件夹中。

path/to/your/new/apache2.conf -> 请根据您的自定义 000-default.conf / 000-default-le-ssl.conf 文件的位置更改路径，如：/share/apache2/000-default.conf <br />
更多信息： <https://cwiki.apache.org/confluence/display/HTTPD/ExampleVhosts><br /> <br />
请注意，如果您使用自定义 apache2 配置文件并且收到任何 apache2 错误，我将不提供任何支持！

### 选项: `website_name`

如果您启用了 ssl 为 true，则此选项是必需的。如果不使用 SSL，只需在此处放入任何内容，因为无关紧要。

### 选项: `username`

此选项是可选的。该用户用于访问网页文件（而非网站本身）。它将把所有网页文件的所有者从 "root" 更改为此新所有者。

这不用于网站的认证。如果您想要此功能，请查看 [网站认证](#网站认证)

### 选项: `password`

此选项是可选的。一些自托管网站需要认证密码以访问 docker 镜像中的文件。#50

这不用于网站的认证。如果您想要此功能，请查看 [网站认证](#网站认证)

### 选项: `ssl`

启用/禁用网页界面的 SSL (HTTPS)。

如果您需要自签名证书，请查看我的 openssl 附加组件： <https://github.com/FaserF/hassio-addons/tree/master/openssl>

**注意**： _文件必须存储在 `/ssl/` 中，这是默认的_

### 选项: `init_commands`

此选项是可选的。如果您需要某些特殊的软件包或命令，可以使用此选项进行安装/使用。 #124

如果您遇到任何问题，请在提交错误报告之前删除此选项！

### 配置示例

推荐的附加组件配置示例：

```yaml
document_root: /share/htdocs
php_ini: default
default_conf: default
default_ssl_conf: default
website_name: mywebsite.com
ssl: true
certfile: fullchain.pem
keyfile: privkey.pem
```

---

## 🔐 认证

`username` 和 `password` 字段用于保护 `/share/apache` 目录中的文件（例如，配置或日志）。它们**不**用于实际托管的网页。

要保护网页内容，请使用 `.htaccess` 和 `.htpasswd` 文件。

### 示例：创建 `.htpasswd`

```bash
htpasswd -c /share/htdocs/.htpasswd myuser
```

然后在您的 `.htaccess` 文件中引用它，如下所示：

```
AuthType Basic
AuthName "Restricted Content"
AuthUserFile /share/htdocs/.htpasswd
Require valid-user
```

---

## 🧩 Ingress

该附加组件支持 ingress（通过 Home Assistant UI 访问）。但是，请注意：

- 基本 HTML 页面可以完美工作。
- 使用完整认证、重定向链或 WebSockets 的复杂应用程序在 ingress 中可能无法很好工作。
- 为了最佳兼容性，建议通过本地 IP 和暴露端口访问。

---

## 🐬 MariaDB 使用

如果您想将 PHP 应用程序（如 WordPress 或 phpMyAdmin）连接到官方 MariaDB 附加组件：

- 使用 `core-mariadb` 作为主机名。
- 端口： `3306`
- 用户名/密码：使用 Home Assistant 的 MariaDB 凭据
- 数据库名称：`homeassistant`（默认）

在 PHP 中的示例配置：

```php
$mysqli = new mysqli("core-mariadb", "user", "pass", "homeassistant");
```

---

## ⚠️ 限制

- ✅ 仅在 amd64 上测试过（其他架构可能有效，但未测试）
- ⚠️ 单位 PHP 支持仅在 **完整** 版本中
- 🔒 SSL 需要在 `/ssl/` 中有效的证书
- 🌐 不建议在没有额外加固的情况下直接暴露于互联网
- 🧩 WordPress 兼容性有限 — 请考虑 [专用 WordPress 附加组件](https://github.com/FaserF/hassio-addons/pull/202)

---

## 🙋 支持

如果您遇到问题或有功能请求，请在 GitHub 上打开一个问题：
👉 [GitHub Issues](https://github.com/FaserF/hassio-addons/issues)

---

## 📝 许可证

该项目根据 MIT 许可证授权。

特此免费授权任何获得本软件及相关文档文件（“软件”）副本的人，不受限制地处理该软件，包括但不限于使用、复制、修改、合并、出版、分发、再许可证和/或出售该软件的副本，并允许向其提供软件的人这样做，前提是以下条件：

相应的版权声明和本许可声明应包含在所有副本或实质性部分的软件中。

该软件是“按原样”提供的，不提供任何种类的保证，无论是明示或暗示，包括但不限于对适销性、特定用途的适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对因使用或其他交易而引起的任何索赔、损害或其他责任（无论是在合同、侵权或其他方面）承担责任。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2025.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg