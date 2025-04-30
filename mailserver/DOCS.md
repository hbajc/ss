# Home Assistant 插件：邮件服务器

带有 Postfixadmin Web 界面的 Postfix/Dovecot 邮件服务器...

![支持 aarch64 架构][aarch64-shield] ![支持 amd64 架构][amd64-shield]
![支持 armv7 架构][armv7-shield] ![支持 i386 架构][i386-shield]

## 关于

重要提示：该插件需要安装并运行 MariaDB 插件！

该插件是实验性的，提供了一个适用于您域的邮件服务器。
还可以在 Postfix Admin Web 界面中配置其他电子邮件域和帐户。

该插件使用以下端口：

smtp：端口 25、465 和 587
imap(s)：993

可以在配置的网络部分更改这些端口。

如果您勇敢，可以考虑将邮件服务器暴露到互联网。
请参见以下说明：

要从互联网接收邮件，必须在路由器中添加 SMTP 端口进行重定向。
所需的 MX 和 A 记录必须在 DNS 中注册。
如果您希望能够从网络外部检查电子邮件，则 IMAP 端口也必须转发。

默认设置将使用 Dovecot 在初始设置期间创建的自签名证书。这可以用于测试，但应该使用“真实”证书。

配置选项 "letsencrypt_certs" 设置为 "true" 时，将使用 Home Assistant 中 /ssl 目录下的 fullchain.pem 和 privkey.pem。

## 安装

按照以下步骤在您的系统上安装插件：

添加存储库 `https://github.com/erik73/hassio-addons`。
找到“邮件服务器”插件并点击它。
点击“安装”按钮。

## 如何使用

### 启动插件

安装后，您将看到一个默认和示例配置。

调整插件配置以满足您的要求。
点击“保存”按钮保存插件配置。
启动插件。

## 配置

示例配置：

```yaml
my_hostname: mydomain.no-ip.com
domain_name: mydomain.no-ip.com
admin_user: admin
admin_password: admin
letsencrypt_certs: false
enable_mailfilter: false
message_size_limit: 10
```

请注意：在插件启动期间，会在 MariaDB 插件中创建一个数据库。
在创建数据库后，当前无法更改用户凭据或 domain_name。
更改这些选项的唯一方法是删除 Postfix Admin 数据库并重启插件。使用 phpMyAdmin 插件删除数据库。

### 选项：`my_hostname` （必填）

您的邮件服务器的主机名。它应与您在 DNS 中的 A 记录相对应。

#### 选项：`domain_name` （必填）

这是您希望接收邮件的域名。
可以在 postfixadmin 界面中添加其他域。

#### 选项：`admin_user` （必填）

Postfixadmin 中的管理员用户名。要登录到 Web 界面，您必须使用 FQDN。例如：admin@mydomain.no-ip.com。
在当前版本的插件中，创建数据库后无法更改此项。

#### 选项：`admin_password` （必填）

管理员用户的密码。
在当前版本的插件中，创建数据库后也无法更改此项。

#### 选项：`letsencrypt_certs` （必填）

如果您使用 Let's Encrypt 插件或以其他方式在 HA 实例的 /ssl 文件夹中安装了证书，此选项将
使用这些证书用于 SMTP 和 IMAP 服务。

文件应该命名为 fullchain.pem 和 privkey.pem。

#### 选项：`message_size_limit` （必填）

配置单个消息/邮件的最大大小（以 MB 计）。
大于此大小的消息将被拒绝。
如果希望与常见云邮件提供商最佳兼容，使用 50 MB。
默认值：10

#### 选项：`enable_mailfilter` （必填）

这将启用与此存储库中的可选 Mailfilter 插件的通信。
它将使 Postfix 扫描电子邮件以查找垃圾邮件和病毒，并包括可选的 DKIM 签名。
为了能够成功从您的主机发送电子邮件，而不冒着被拒绝或被归类为垃圾邮件的风险，DKIM 签名是必须的。
您还必须配置 DNS 服务器提供 SPF 和 DMARC。
如果 DKIM、SPF 和 DMARC 听起来太复杂，请使用 smtp_relay 选项。

病毒扫描需要大量内存，建议使用 4-8 GB。
在 Mailfilter 插件中默认关闭病毒扫描。

#### 选项：`smtp_relayhost` （可选）

使用此可选设置为外发邮件使用中继服务器。ISP 通常会屏蔽您网络的外发邮件。
在这种情况下，您可以使用 ISP 的 SMTP 中继主机来绕过此限制。
输入主机名时最好用方括号括起来。这可以禁用该主机的 MX 查询，推荐使用。您还可以指定要使用的端口。
例如：

```yaml
smtp_relayhost: [smtp.relay.com]:587
```

上述示例表示使用端口 587 进行提交。
如果您的 ISP 需要用户名和密码，请使用下面的选项。

#### 选项：`smtp_relayhost_credentials` （可选）

使用此可选设置与您指定的中继服务器进行身份验证。
正确的语法是 username:password，您可以从提供商处获取这些信息。
仅在您知道确实需要用户凭据才能中继时使用此选项。

## 支持

有问题吗？

您可以在这里 [提交问题][issue] GitHub。

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
[issue]: https://github.com/erik73/addon-mail/issues
[repository]: https://github.com/erik73/hassio-addons