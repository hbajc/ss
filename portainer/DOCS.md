Portainer 可以用于在 docker 容器中执行自定义命令。它是一个开源轻量级管理 UI，可以让您轻松管理 Docker 主机或 Docker swarm 集群。

# 快速开始
- 使用此链接添加我的仓库
[![Add repository on my Home Assistant][repository-badge]][repository-url]
- 从我的仓库安装 portainer 附加组件
- 在附加组件的配置面板中，您可以更改密码
- 在附加组件的主页面中，禁用“保护模式”，然后启动附加组件
- 登录（默认用户名是 `admin`，默认密码是 `homeassistant`）
- 点击页面中央的环境中的 `Primary`
- 在左侧菜单栏中点击 `Containers`
- 增加每页项目的数量，以查看所有附加组件
- 点击选定附加组件名称旁边的符号 `>_` 以打开控制台页面
- 更改用户名，或者通常只需点击连接
- 输入您的命令，您可以完全访问该特定容器的终端（这不会影响您的 HA 系统的其他部分）

# 对您的系统的影响
- 安装或运行 portainer 不会对系统产生影响
- 手动安装自定义容器将把您的 HA 状态修改为不受支持/不健康状态。您将无法升级 Home Assistant 和您可能拥有的任何附加组件。停止此自定义容器将重置为正常状态

# 小贴士和技巧

## 重置数据库
只需在您的附加组件选项中更改密码，数据库将被重置

## 60 秒超时
该附加组件包括非常长的超时。然而，如果您使用另一个代理层，例如附加组件 nginx 代理管理器，默认超时将为 60 秒。您需要调整代理层以增加超时。更多细节请参见： https://github.com/portainer/portainer/issues/2953#issuecomment-1235795256

## 进一步参考
- 这里有一份全面的使用指南： https://codeopolis.com/posts/beginners-guide-to-portainer/
- HA 社区论坛上有关 portainer 的旧页面： https://community.home-assistant.io/t/home-assistant-community-add-on-portainer

[repository-badge]: https://img.shields.io/badge/Add%20repository%20to%20my-Home%20Assistant-41BDF5?logo=home-assistant&style=for-the-badge
[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons