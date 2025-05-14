# 家庭助理社区插件：OpenSSL
![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield] ![支持 armhf 架构][armhf-shield] ![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]
![项目维护][maintenance-shield]

OpenSSL - 为 Homeassistant 操作系统提供自签名证书

## 关于

OpenSSL 是一个软件库，用于在计算机网络上保护通信，防止窃听或识别另一端的通信方。它被许多互联网服务器广泛使用，包括大多数 HTTPS 网站。

OpenSSL 包含 SSL 和 TLS 协议的开源实现。核心库用 C 编程语言编写，实施基本的加密功能并提供各种实用函数。支持使用 OpenSSL 库的多种计算机语言的包装器也可用。

OpenSSL 软件基金会 (OSF) 代表 OpenSSL 项目在大多数法律事务中，包括贡献者许可协议、管理捐赠等。OpenSSL 软件服务 (OSS) 也代表 OpenSSL 项目，提供支持合同。

## 安装

[![FaserF 家庭助理插件](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FFaserF%2Fhassio-addons)
<br />
该插件的安装非常简单，与安装其他自定义家庭助理插件没有什么不同。<br />
只需点击上面的链接或将我的仓库添加到 hassio 插件库： <https://github.com/FaserF/hassio-addons>

启动插件后，将会创建并放置一个自签名证书到：
/ssl/key_openssl.pem
/ssl/cert_openssl.pem

然后可以被其他插件使用，例如我的 apache2 网络服务器插件。
如果证书即将过期，只需重新启动一次插件，将会生成新的证书。
警告：插件重启后，以上命名的旧证书将被删除并覆盖！

## 配置

**注意**：_修改配置后，请记得重启插件。_

示例插件配置：

```yaml
website_name: mywebsite.ddns.net
```

**注意**：_这只是一个示例，请不要复制粘贴！创建你自己的！_

### 选项：`website_name`

这个选项是必需的。这将是自签名证书的网站名称。

## 支持

有问题吗？

你可以在这里 [打开一个问题][issue] GitHub。
请记住，这个软件仅在 Tinkerboard 上的 armv7 运行时经过测试。

## 作者及贡献者

原程序来自 OpenSSL 项目。有关更多信息，请访问此页面： <https://www.openssl.org/>
该 hassio 插件由 [FaserF] 提供。

## 许可证

MIT 许可证

版权所有 (c) 2019-2021 FaserF & OpenSSL 项目

特此免费授权任何获得本软件及相关文档文件（“软件”）副本的人，不受限制地处理软件，包括但不限于使用、复制、修改、合并、出版、分发、再授权和/或销售软件副本，并允许提供软件的人这样做，受以下条件的限制：

上述版权声明和本许可声明应包含在所有软件的副本或重要部分中。

该软件是按“原样”提供的，不提供任何类型的担保，明确或暗示，包括但不限于对适销性、特定用途适用性和不侵权的担保。在任何情况下，作者或版权持有人均不对因使用该软件或与该软件相关的使用或其他交易而引起的任何索赔、损害或其他责任承担责任，无论是在合同、侵权或其他行动中。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[FaserF]: https://github.com/FaserF/
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/FaserF/hassio-addons/issues
[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg