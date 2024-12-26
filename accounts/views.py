from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout

# 登录接口
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]  # 允许所有用户访问

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # 检查输入的用户名和密码是否为空
        if not username or not password:
            return Response({
                'detail': '用户名和密码为必填项。'
            }, status=status.HTTP_400_BAD_REQUEST)

        # 用户认证
        user = authenticate(request, username=username, password=password)

        # 如果认证通过，登录用户并返回成功消息
        if user is not None:
            login(request, user)
            return Response({
                'message': '登录成功！',
                'user': {
                    'username': user.username,
                    'email': user.email,
                }
            }, status=status.HTTP_200_OK)

        # 如果认证失败，返回错误信息
        return Response({
            'detail': '无效的用户名或密码。'
        }, status=status.HTTP_400_BAD_REQUEST)


# 登出接口
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # 只有已认证用户可以访问

    def post(self, request):
        logout(request)  # 注销用户
        return Response({
            'message': '登出成功！'
        }, status=status.HTTP_200_OK)
