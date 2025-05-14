# Home Assistant Community Add-on: Apache2
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]
![项目维护][maintenance-shield]

Homeassistant OS 的 Apache2 网络服务器

![Ingress 支持](../_images/apache2/ingress.png)

## 关于

Apache HTTP 服务器项目旨在为现代操作系统（包括 UNIX 和 Windows）开发和维护一个开源 HTTP 服务器。该项目的目标是提供一个安全、有效且可扩展的服务器，以便与当前的 HTTP 标准同步提供 HTTP 服务。<br />
Apache HTTP 服务器（“httpd”）于 1995 年推出，并自 1996 年 4 月以来一直是互联网上最流行的 Web 服务器。它在 2020 年 2 月庆祝了其作为项目的 25 周年。<br />
Apache HTTP 服务器是 Apache 软件基金会的一个项目。

## 不同版本

### 完整版
[完整的 Apache2 版本](https://github.com/FaserF/hassio-addons/tree/master/apache2) 包含 MariaDB 和常用的 PHP 8 模块。<br />
此 Docker 镜像包含：apache2 php84-apache2 libxml2-dev apache2-utils apache2-mod-wsgi apache2-ssl mariadb-client ffmpeg<br />
将安装以下 php84 扩展：php84 php84-dev php84-fpm php84-mysqli php84-opcache php84-gd zlib php84-curl php84-phar php84-mbstring php84-zip php84-pdo php84-pdo_mysql php84-iconv php84-dom php84-session php84-intl php84-soap php84-fileinfo php84-xml php84-ctype php84-pecl-xdebug php84-pdo_sqlite php84-tokenizer php84-exif php84-xmlwriter php84-cgi php84-simplexml php84-gd php84-json php84-imap php84-apcu php84-simplexml php84-sockets<br />
Mosquitto & Mosquitto Dev<br />
同时它还包含 PHP 语言环境。

### 最小版
[最小版](https://github.com/FaserF/hassio-addons/tree/master/apache2-minimal) 的 Apache2 附加组件不包括 MariaDB 和 PHP 模块。<br />
此 Docker 镜像包含：apache2 libxml2-dev apache2-utils apache2-mod-wsgi apache2-ssl

### 含 MariaDB 的最小版
[含 MariaDB 和一些 PHP 模块的最小版](https://github.com/FaserF/hassio-addons/tree/master/apache2-minimal-mariadb) 的 Apache2 附加组件。<br />
此 Docker 镜像包含：apache2 php84-apache2 libxml2-dev apache2-utils apache2-mod-wsgi apache2-ssl mariadb-client<br />
将安装以下 php84 扩展：php84 php84-mysqli php84-opcache php84-curl php84-mbstring php84-zip

## 安装

[![FaserF Homeassistant Addons](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
安装此附加组件非常简单，与安装任何其他自定义 Home Assistant 附加组件没有区别。<br />
只需点击上面的链接或将我的仓库添加到 hassio 附加组件库：<https://github.com/FaserF/hassio-addons>

将你的网页文件放到 /share/htdocs<br />
你的 index.html 应该放置的示例文件位置：/share/htdocs/index.html <br />

如果你想将网站与 MariaDB 数据库集成，请确保已安装 MariaDB 附加组件！

## 配置

**注意**：_记得在配置更改时重启附加组件。_

附加组件配置示例：

```yaml
document_root: /media/apache2
php_ini: /share/apache2/php.ini
default_conf: /share/apache2/000-default.conf
default_ssl_conf: get_file
website_name: itdoesntmatter_as_ssl_is_set_to_false
username: apache
password: mySecretPassword
ssl: false
certfile: itdoesntmatter_as_ssl_is_set_to_false
keyfile: itdoesntmatter_as_ssl_is_set_to_false
```
<br />
推荐的附加组件配置示例：

```yaml
document_root: /share/htdocs
php_ini: default
default_conf: default
default_ssl_conf: default
website_name: mywebsite.ddns.net
ssl: true
certfile: fullchain.pem
keyfile: privkey.pem
```

**注意**：_这只是一个示例，请勿复制粘贴！创建你自己的！_

### 选项： `document_root`

此选项是必需的。根据你的 Home Assistant 安装中根网页文件夹的位置进行更改。

注意：必须在 /share 或 /media 文件夹中的某个地方！其他文件夹对这个附加组件是不可见的。

### 选项： `php_ini`

你可以选择以下选项：

default -> 使用默认 php84 php.ini 文件

get_file -> 复制默认的 php84 php.ini 文件从附加组件到 /share/apache2addon_php.ini

path/to/your/new/php.ini -> 请根据你的自定义 php.ini 文件的位置进行更改，例如：/share/apache2/php.ini

### 选项： `default_conf` & `default_ssl_conf`

你可以选择以下选项：

default -> 使用默认的 apache2 附加组件文件

get_config -> 获取默认 apache2 附加组件配置文件的副本到你的 /share 文件夹。

path/to/your/new/apache2.conf -> 请根据你的自定义 000-default.conf / 000-default-le-ssl.conf 文件的位置进行更改，例如：/share/apache2/000-default.conf <br />
更多信息： <https://cwiki.apache.org/confluence/display/HTTPD/ExampleVhosts><br /> <br />
请注意，如果你使用自定义 apache2 配置文件并遇到任何 apache2 错误，我将不会提供任何支持！

### 选项： `website_name`

如果你将 SSL 设置为 true，此选项是必需的。如果不使用 SSL，填入任何内容即可，因为这无关紧要。

### 选项： `username`

此选项是可选的。该用户用于访问网页文件（而不是网站本身）。它会将所有网页文件的所有者从“root”更改为这个新所有者。

这不用于你网站的身份验证。如果你想要，请查看 [你网站的身份验证](#authentification-for-your-website)

### 选项： `password`

此选项是可选的。某些自托管网站需要身份验证密码以访问 Docker 镜像中的文件。 #50

这不用于你网站的身份验证。如果你想要，请查看 [你网站的身份验证](#authentification-for-your-website)

### 选项： `ssl`

在 Web 界面上启用/禁用 SSL (HTTPS)。

如果你需要自签名证书，请查看我的 openssl 附加组件： <https://github.com/FaserF/hassio-addons/tree/master/openssl>

**注意**：_文件必须存储在 `/ssl/` 中，这里是默认位置_

### 选项： `init_commands`

此选项是可选的。如果你需要一些特殊的软件包或命令，可以使用此选项进行安装/使用。 #124

如果你遇到任何问题，请在提交错误报告之前删除此选项！

## 你网站的身份验证
使用 .htaccess 文件和 .htpasswd 文件组合来实现： <https://www.htaccessredirect.net/>

示例 .htaccess 文件：

```bash
AuthType Basic
AuthName "我的 Web 服务器身份验证"
AuthUserFile /share/.htpasswd
Require valid-user
```

## Ingress

此附加组件支持 Homeassistant Ingress。到目前为止，似乎仅在启用 SSL 时可以正常工作！
另外，抱歉，我无法支持你所有的网站。基本的 HTML 网站在 ingress 中效果很好，而页面越复杂，支持 ingress 的难度就越大。

## 支持

有问题或疑问？

你可以在这里 [提出问题][issue] GitHub。
请记住，该软件仅在树莓派 4 上的 armv7 中经过测试。

## 作者和贡献者

原始程序来自 Apache 项目。有关更多信息，请访问此页面： <https://httpd.apache.org/>
hassio 附加组件由 [FaserF] 提供。

## 许可证

MIT 许可证

版权 (c) 2019-2023 FaserF & Apache 项目

特此免费授予任何获取本软件及相关文档文件（“软件”）副本的人，无限制地处理该软件，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或出售该软件的副本，以及允许向其提供该软件的人这样做，前提是满足以下条件：

上述版权声明和本许可证声明应包含在所有副本或重大部分软件中。

该软件按“原样”提供，不提供任何种类的担保，明示或暗示，包括但不限于对适销性、特定用途适用性和非侵权的担保。在任何情况下，作者或版权持有者均不对因使用该软件或其他交易的结果而产生的任何索赔、损害或其他责任承担责任，无论是在合同诉讼、侵权或其他情况下。

[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg
[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[FaserF]: https://github.com/FaserF/
[issue]: https://github.com/FaserF/hassio-addons/issues