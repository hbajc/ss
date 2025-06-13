Portainer 可以用来在 Docker 容器中执行自定义命令。它是一个开源的轻量级管理用户界面，允许你轻松管理 Docker 主机或 Docker 集群。

# 快速开始
- 使用此链接添加我的仓库
[![Add repository on my Home Assistant][repository-badge]][repository-url]
- 从我的仓库中安装 Portainer 插件
- 在插件的配置面板中，你可以更改密码
- 在插件的主页中，禁用 “保护模式”，然后启动插件
- 登录（默认用户名是 `admin`，默认密码是 `homeassistant`）
- 点击环境中的 `Primary`（在页面中央）
- 点击左侧菜单栏中的 `Containers`
- 增加每页项目的数量以查看所有插件
- 点击所选插件名称旁边的符号 `>_` 以打开控制台页面
- 更改用户名，或更常见的是直接点击连接
- 输入你的命令，你对这个特定容器的终端有完全访问权限（这不会影响你的 HA 系统的其他部分）

# 对你的系统的影响
- 安装或运行 Portainer 不会对系统产生影响
- 手动安装自定义容器将使你的 HA 状态更改为不支持/不健康的状态。你将无法升级 Home Assistant 和任何你可能拥有的插件。停止此自定义容器将重置为正常状态

# 小贴士和技巧

## 重置数据库
只需在你的插件选项中更改密码，数据库将会被重置

## 60秒超时
插件包含一个非常长的超时。不过，如果你使用了其他层的代理，如插件 nginx 代理管理器，它默认的超时为 60秒。你需要调整代理层以增加超时。更多详细信息请见： https://github.com/portainer/portainer/issues/2953#issuecomment-1235795256

## 进一步参考
- 这是使用它的完整指南： https://codeopolis.com/posts/beginners-guide-to-portainer/
- 关于 Portainer 的旧页面在 HA 社区论坛： https://community.home-assistant.io/t/home-assistant-community-add-on-portainer

[repository-badge]: https://img.shields.io/badge/Add%20repository%20to%20my-Home%20Assistant-41BDF5?logo=home-assistant&style=for-the-badge
[repository-url]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Falexbelgium%2Fhassio-addons