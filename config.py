from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = '批量创建用户'

    def handle(self, *args, **options):
        # 准备用户数据
        user_data = [
            {'username': 'user_1001', 'email': 'user1@example.com', 'jlzs': 'jlzs'},
            {'username': 'user_1002', 'email': 'user2@example.com', 'jlzs': 'jlzs'},
            # 可按需添加更多用户数据
        ]

        users = []
        for data in user_data:
            user = User(username=data['username'], email=data['email'])
            user.set_password(data['password'])
            users.append(user)

        # 批量创建用户
        User.objects.bulk_create(users)

        self.stdout.write(self.style.SUCCESS('成功批量创建用户！'))


