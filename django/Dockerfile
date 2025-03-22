# 使用官方 Python 运行时作为基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /code

# 复制 requirements.txt
COPY requirements.txt requirements.txt

# 使用国内 PyPI 镜像源安装依赖
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 复制项目源代码
COPY . .

# 设置环境变量
ENV DJANGO_SETTINGS_MODULE=user_management.settings