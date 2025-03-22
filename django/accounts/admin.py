from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import UserProfile
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'phone_number', 'address', 'birth_date', 'gender', 'register_date', 'get_age', 'show_profile_picture')
    list_filter = ('gender',)
    search_fields = ('user__username', 'phone_number', 'address')
    fieldsets = (
        ('基本信息', {
            'fields': ('user', 'gender', 'birth_date', 'profile_picture')
        }),
        ('联系信息', {
            'fields': ('phone_number', 'address', 'social_media_link')
        }),
        ('个人信息', {
            'fields': ('bio', 'occupation', 'interests', 'education')
        }),
        ('注册信息', {
            'fields': ('register_date',)
        }),
    )

    @admin.display(description='用户照片')
    def show_profile_picture(self, obj):
        if hasattr(obj.profile_picture, 'url'):
            # 在custom.js里面实现了show_pic函数，onclick进行调用
            div = f"""<img id='icon_{obj.id}' src='{obj.profile_picture.url}' width='100px' onclick='show_pic("{obj.profile_picture.url}")' />"""
            return mark_safe(div)
        return ''


    class Media:
        # 使用 settings.STATIC_URL 来拼接静态文件路径
        js = (f'{settings.STATIC_URL}js/custom.js',)







admin.site.register(UserProfile, UserProfileAdmin)
admin.site.site_header = '简历助手-用户管理系统'  # 设置header
admin.site.site_title = '简历助手-用户管理系统'   # 设置title
admin.site.index_title = '简历助手-用户管理系统'