from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户表
class User(AbstractUser):
    nickname = models.CharField(max_length=16, unique=True, null=True, blank=True, verbose_name='昵称')
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    # 0为男，1为女
    gender = models.IntegerField(choices=((0, "男"), (1, "女")), default=0, verbose_name="性别")
    photo = models.ImageField(upload_to="user/photo", null=True, blank=True, verbose_name='头像')
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True, verbose_name='手机号')
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True, verbose_name='邮箱')
    desc = models.CharField(max_length=140, null=True, blank=True, verbose_name='个人简介')
    addtime = models.DateField(auto_now_add=True, verbose_name='注册日期')

    class Meta:
        # 指定在admin管理界面中显示中文,表示单数形式的显示
        verbose_name = '用户表'
        # 指定在admin管理界面中显示中文,表示复数形式的显示
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 用户留言表
class Leavemsg(models.Model):
    content = models.CharField(max_length=140, verbose_name="用户留言")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='留言用户')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='留言时间')

    class Meta:
        verbose_name = '用户留言表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nickname
