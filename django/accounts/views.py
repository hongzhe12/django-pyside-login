from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# 登录接口
@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 检查输入的用户名和密码是否为空
        if not username or not password:
            return JsonResponse({
                'detail': '用户名和密码为必填项。'
            }, status=400)

        # 用户认证
        user = authenticate(request, username=username, password=password)

        # 如果认证通过，登录用户并返回成功消息
        if user is not None:
            login(request, user)
            return JsonResponse({
                'message': '登录成功！',
                'user': {
                    'username': user.username,
                    'email': user.email,
                }
            }, status=200)

        # 如果认证失败，返回错误信息
        return JsonResponse({
            'detail': '无效的用户名或密码。'
        }, status=400)


# 登出接口
@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    def post(self, request):
        logout(request)  # 注销用户
        return JsonResponse({
            'message': '登出成功！'
        }, status=200)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '注册成功！现在你可以使用注册信息登录了。')
            form = UserRegistrationForm()  # 清空表单
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

