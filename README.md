### 一、接口概述
该文档描述了两个与用户认证相关的接口，分别是登录接口和登出接口。这些接口使用 Django REST framework 实现，提供了用户登录和登出的功能。

### 二、登录接口

#### 1. 基本信息
- **接口地址**：`/login/`
- **请求方法**：`POST`
- **权限要求**：允许所有用户访问

#### 2. 请求参数
| 参数名 | 类型 | 是否必传 | 描述 |
| ---- | ---- | ---- | ---- |
| username | string | 是 | 用户的用户名 |
| password | string | 是 | 用户的密码 |

#### 3. 请求示例
```json
{
    "username": "testuser",
    "password": "testpassword"
}
```

#### 4. 响应信息
- **成功响应（HTTP 200 OK）**
```json
{
    "message": "登录成功！",
    "user": {
        "username": "testuser",
        "email": "testuser@example.com"
    }
}
```
- **失败响应（HTTP 400 BAD REQUEST）**
  - 当用户名或密码为空时：
```json
{
    "detail": "用户名和密码为必填项。"
}
```
  - 当用户名或密码无效时：
```json
{
    "detail": "无效的用户名或密码。"
}
```

### 三、登出接口

#### 1. 基本信息
- **接口地址**：`/logout/`
- **请求方法**：`POST`
- **权限要求**：只有已认证用户可以访问

#### 2. 请求参数
无

#### 3. 请求示例
无

#### 4. 响应信息
- **成功响应（HTTP 200 OK）**
```json
{
    "message": "登出成功！"
}
```