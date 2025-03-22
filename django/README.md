### 初始化
```shell
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py runserver 8080

python manage.py collectstatic --noinput
ls -l static/admin/simpleui-x/elementui/theme-chalk/index.css
ls -l /static/admin/simpleui-x/elementui/theme-chalk/index.css
```

### 配置Nginx Proxy Manager，添加到advance中
```bash
 location /static/ {
    alias /static/;  # 指定静态文件的路径别名
    expires 30d;
    add_header Cache-Control "public";
}
location /media/ {
    alias /media/;  # 指定媒体文件的路径别名
    expires 30d;
    add_header Cache-Control "public";
}
location /favicon.ico {
    alias /static/img/favicon.ico;  # 指定网站图标的路径
    expires 30d;
    add_header Cache-Control "public";
}
```