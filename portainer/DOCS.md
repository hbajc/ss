Portainer 可以用来在 Docker 容器中执行自定义命令。它是一个开源的轻量级管理用户界面，允许你轻松管理 Docker 主机或 Docker 集群。

# 快速开始
- 使用此链接添加我的存储库
[![将存储库添加到我的 Home Assistant][repository-badge]][repository-url]
- 从我的存储库安装 Portainer 附加组件
- 在附加组件的配置面板中，你可以更改密码
- 在附加组件的主页中，禁用“保护模式”，然后启动附加组件
- 登录（默认用户名为 `admin`，默认密码为 `homeassistant`）
- 点击环境中的 `Primary`（位于页面中间）
- 点击左侧菜单栏中的 `Containers`
- 增加每页项目的数量，以查看所有附加组件
- 点击所选附加组件名称旁边的符号 `>_` 以打开控制台页面
- 更改用户名，或者更常见的是直接点击连接
- 输入你的命令，你可以完全访问这个特定容器的终端（这不会影响你的 HA 系统的其他部分）

# 对系统的影响
- 安装或运行 Portainer 并不会对系统产生影响
- 手动安装自定义容器会将你的 HA 状态修改为不受支持/不健康状态。你将无法升级 Home Assistant 和任何附加组件。停止这个自定义容器将重置为正常状态

# 提示和技巧

## 重置数据库
只需在附加组件选项中更改密码，数据库将被重置

## 60 秒超时
附加组件包含一个非常长的超时。然而，如果你使用其他层的代理，例如附加组件 Nginx 代理管理器，默认超时为 60 秒。你需要调整代理层以增加超时。更多详细信息请见: https://github.com/portainer/portainer/issues/2953#issuecomment-1235795256

## 进一步参考
- 这是使用它的完整指南: https://codeopolis.com/posts/beginners-guide-to-portainer/
- 关于 Portainer 的旧页面在 HA 社区论坛上: https://community.home-assistant.io/t/home-assistant-community-add-on-portainer

[repository-badge]: https://img.shields.io/badge/Add%20repository%20to%20my-Home%20Assistant-41BDF5?logo=home-assistant&style=for-the-badge
[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons