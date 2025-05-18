## 配置

请查看 Tandoor Recipes 文档： https://docs.tandoor.dev/install/docker/

```yaml
必填：
    "ALLOWED_HOSTS": "你的系统网址", # 你需要输入你的 homeassistant URLs（用逗号分隔，且不带空格）以允许流量进入
    "DB_TYPE": "list(sqlite|postgresql_external)" # 要使用的数据库类型。
    "SECRET_KEY": "str", # 你的秘密密钥
    "PORT": 9928 # 默认情况下，webui 可在 http://HAurl:9928 上使用。如果需要更改端口，永远不要在应用中进行更改，只能通过此选项。
    "Environment": 0|1 # 1 为调试模式，0 为正常模式。除非在积极开发，否则应在正常模式下运行。
    "GUNICORN_MEDIA": 0|1 # 1 启用 gunicorn 媒体托管。这不推荐。你应该使用 nginx 服务器来托管媒体 - 请参见文档。
可选：
    "POSTGRES_HOST": "str?", # postgresql_external 所需
    "POSTGRES_PORT": "str?", # postgresql_external 所需
    "POSTGRES_USER": "str?", # postgresql_external 所需
    "POSTGRES_PASSWORD": "str?", # postgresql_external 所需
    "POSTGRES_DB": "str?" # postgresql_external 所需
    "externalfiles_folder": "str?" # 一个你想要映射到 tandoor 的文件夹。由于 /share/ 和 /media/ 已经映射，因此不需要。这将创建文件夹（如果尚不存在）。
```
### Mariadb
Mariadb 是一个在 home assistant 社区中流行的附加组件，但不被 Tandoor Recipes 应用支持。

### 调试模式
这就是 "Environment" 设置。
0 为正常模式  
1 为调试模式。

### 认证
使用外部认证。Tandoor Recipes 支持这一点，但尚未实现。

### Gunicorn 媒体
禁用 gunicorn 媒体是个好主意，但需要一个正在运行的 Web 服务器来托管媒体文件。Web 服务器应映射 `/media/`。  
有关更多信息，请参见 https://docs.tandoor.dev/install/docker/#nginx-vs-gunicorn。  
0 表示 gunicorn 被禁用 - 媒体在没有 nginx Web 服务器的情况下无法工作。  
1 表示启用 gunicorn - 媒体将使用 gunicorn 托管，这不推荐。

### 外部食谱文件

目录 `/config/addons_config/tandoor_recipes/externalfiles` 可用于将外部文件导入到 Tandoor。你可以在 Docker 中将其映射到 /opt/recipes/externalfiles。根据此处的说明：https://docs.tandoor.dev/features/external_recipes/
目录 `/config`、`/media/` 和 `/share/` 都已经映射到插件中。你可以在这些位置的任何位置手动创建一个文件夹并将其映射到 tandoor：
- 在你想要的位置创建一个目录，例如 `/share/tandoor/recipebook/`
- 在 tandoor 中创建一个外部存储的位置 - `/share/tandoor/`
- 监视特定文件夹 - `/share/tandoor/recipebook/`
- 立即同步
- 导入。