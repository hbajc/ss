Portainer可以用来在Docker容器中执行自定义命令。它是一个开源的轻量级管理用户界面，允许您轻松管理Docker主机或Docker集群。

# 快速开始
- 使用此链接添加我的库
[![在我的Home Assistant上添加库][repository-badge]][repository-url]
- 从我的库安装Portainer插件
- 在插件的配置面板中，您可以更改密码
- 在插件的主页中，禁用“保护模式”，然后启动插件
- 登录（默认用户名是`admin`，默认密码是`homeassistant`）
- 在环境中点击`Primary`（在页面中央）
- 在左侧菜单栏中点击`Containers`
- 增加每页显示的项目数量以查看您所有的插件
- 点击您所选插件名称旁边的符号`>_`以打开控制台页面
- 更改用户名，或者更常见地，只需点击连接
- 输入您的命令，您对该特定容器的终端拥有完全访问权限（这不会影响您HA系统的其他部分）

# 对您系统的影响
- 安装或运行Portainer没有影响
- 手动安装自定义容器会将您的HA状态修改为不支持/不健康状态。您将无法升级Home Assistant和您可能拥有的任何插件。停止该自定义容器将重置正常状态

# 小贴士和技巧

## 重置数据库
只需在您的插件选项中更改密码，数据库将被重置

## 60秒超时
该插件包含一个非常长的超时。然而，如果您使用另一层代理，如插件nginx代理管理器，它将默认为60秒超时。您需要适应代理层以增加超时。更多详细信息请见：https://github.com/portainer/portainer/issues/2953#issuecomment-1235795256

## 进一步参考
- 这是一个完整的使用指南：https://codeopolis.com/posts/beginners-guide-to-portainer/
- 关于Portainer的HA社区论坛旧页面：https://community.home-assistant.io/t/home-assistant-community-add-on-portainer

[repository-badge]: https://img.shields.io/badge/Add%20repository%20to%20my-Home%20Assistant-41BDF5?logo=home-assistant&style=for-the-badge
[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons