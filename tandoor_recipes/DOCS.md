## 配置

请查看 Tandoor Recipes 文档: https://docs.tandoor.dev/install/docker/

```yaml
必需的 :
    "ALLOWED_HOSTS": "你的系统网址", # 你需要输入你的 homeassistant 网址（用逗号分隔，不带空格），以允许流量进入
    "DB_TYPE": "list(sqlite|postgresql_external)" # 要使用的数据库类型。
    "SECRET_KEY": "str", # 你的密钥
    "PORT": 9928 # 默认情况下，webui 可以在 http://HAurl:9928 访问。如果你需要更改端口，应该只通过这个选项进行，而不是在应用内更改
    "Environment": 0|1 # 1 是调试模式，0 是正常模式。除非正在主动开发，否则应在正常模式下运行。
    "GUNICORN_MEDIA": 0|1 # 1 启用 gunicorn 媒体托管。这个不推荐。你应该使用 nginx 服务器来托管你的媒体 - 参见文档。
可选的 :
    "POSTGRES_HOST": "str?", # 需要用于 postgresql_external
    "POSTGRES_PORT": "str?", # 需要用于 postgresql_external
    "POSTGRES_USER": "str?", # 需要用于 postgresql_external
    "POSTGRES_PASSWORD": "str?", # 需要用于 postgresql_external
    "POSTGRES_DB": "str?" # 需要用于 postgresql_external
    "externalfiles_folder": "str?" # 想要映射到 tandoor 的文件夹。由于 /share/ 和 /media/ 已经映射，因此不需要这个文件夹。如果该文件夹不存在，将会被创建。
```
### Mariadb
Mariadb 是 home assistant 社区中一个流行的插件，但不被 Tandoor Recipes 应用所支持。

### 调试模式
这是 "Environment" 设置。
0 是正常模式  
1 是调试模式。

### 身份验证
使用外部身份验证。Tandoor Recipes 支持此功能，但尚未实现。

### Gunicorn 媒体
禁用 gunicorn 媒体是个好主意，但需要运行一个网络服务器来托管媒体文件。网络服务器应该映射 `/media/`。  
有关更多信息，参考 https://docs.tandoor.dev/install/docker/#nginx-vs-gunicorn 。  
0 是 gunicorn 禁用 - 媒体在没有 nginx 网络服务器的情况下无法工作。  
1 是 gunicorn 启用 - 媒体将通过 gunicorn 托管，这并不推荐。

### 外部食谱文件

目录 `/config/addons_config/tandoor_recipes/externalfiles` 可用于将外部文件导入到 Tandoor。你可以在 Docker 中将其映射到 /opt/recipes/externalfiles。具体说明请见这里: https://docs.tandoor.dev/features/external_recipes/
目录 `/config`、`/media/` 和 `/share/` 已映射到插件中。你可以在这些位置中的任何一个手动创建文件夹并映射到 tandoor：
- 在你想要的位置创建一个目录，例如 `/share/tandoor/recipebook/`
- 在 tandoor 中创建一个外部存储位置 - `/share/tandoor/`
- 监视特定文件夹 - `/share/tandoor/recipebook/`
- 立即同步
- 导入。