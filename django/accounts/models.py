from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    # 关联默认的 User 模型，使用一对一关联，当关联的 User 被删除时，此 UserProfile 也会被删除
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("关联用户"))
    # 扩展字段：电话号码，最大长度为 15，允许为空，表单中该字段可以不填写，添加了中文提示和验证器
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=_("电话号码格式：'+999999999'，最多 15 位数字。"))
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True,
                                    verbose_name=_("电话号码"))
    # 扩展字段：地址，最大长度为 200，允许为空，表单中该字段可以不填写，添加了中文提示
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("地址"))
    # 扩展字段：出生日期，允许为空，表单中该字段可以不填写，添加了中文提示
    birth_date = models.DateField(blank=True, null=True, verbose_name=_("出生日期"))
    # 扩展字段：性别，使用选择字段
    GENDER_CHOICES = (
        ('M', _('男')),
        ('F', _('女')),
        ('O', _('其他')),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True, verbose_name=_("性别"))
    # 扩展字段：注册时间，自动记录创建时间
    register_date = models.DateTimeField(default=timezone.now, verbose_name=_("注册时间"))
    # 扩展字段：用户照片，使用 ImageField 存储用户上传的照片
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        verbose_name=_("用户照片")
    )
    # 扩展字段：个人简介，使用 TextField 可以存储较长的文本
    bio = models.TextField(blank=True, null=True, verbose_name=_("个人简介"))
    # 扩展字段：职业，最大长度为 100，允许为空
    occupation = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("职业"))
    # 扩展字段：兴趣爱好，使用 TextField 存储多个兴趣爱好
    interests = models.TextField(blank=True, null=True, verbose_name=_("兴趣爱好"))
    # 扩展字段：教育背景，使用 TextField 存储教育相关信息
    education = models.TextField(blank=True, null=True, verbose_name=_("教育背景"))
    # 扩展字段：社交账号链接，最大长度为 200，允许为空
    social_media_link = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("社交账号链接"))

    def __str__(self):
        return self.user.username

    def get_age(self):
        """
        计算用户的年龄
        """
        if self.birth_date:
            today = timezone.now().date()
            return today.year - self.birth_date.year - (
                        (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return None

    class Meta:
        # 单数形式的中文名称
        verbose_name = "用户资料"
        # 复数形式的中文名称，后台列表页显示的名称
        verbose_name_plural = "用户资料"
