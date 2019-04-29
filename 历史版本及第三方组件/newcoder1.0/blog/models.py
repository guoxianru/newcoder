from django.db import models
from DjangoUeditor.models import UEditorField


# 用户表
class User(models.Model):
    username = models.CharField(max_length=20, verbose_name='用户名')
    nickname = models.CharField(max_length=10, verbose_name='昵称')
    password = models.CharField(max_length=64, verbose_name='密码')
    photo = models.ImageField(upload_to="photo", verbose_name='头像')
    phone = models.CharField(max_length=11, verbose_name='手机号')
    email = models.EmailField(verbose_name='邮箱')
    desc = models.CharField(max_length=140, verbose_name='个人简介')
    date = models.DateField(auto_now_add=True, verbose_name='注册日期')

    def __str__(self):
        return self.nickname

    class Meta:
        # 末尾不加s
        verbose_name_plural = '用户表'
        # 末尾加s
        # verbose_name='标签'


# 文章分类表
class Type(models.Model):
    typename = models.CharField(max_length=20, verbose_name='分类名称')

    def __str__(self):
        return self.typename

    class Meta:
        verbose_name_plural = '文章分类表'


# 文章表
class Article(models.Model):
    title = models.CharField(max_length=40, verbose_name='文章标题')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章作者')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='文章分类')
    date = models.DateTimeField(auto_now_add=True, verbose_name='创作时间')
    pic = models.ImageField(upload_to="pics", verbose_name='文章配图')
    content = UEditorField('内容', width=800, height=500, toolbars="full", imagePath="imgs/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000}, settings={}, command=None, blank=True)
    like = models.IntegerField(default=0, verbose_name='点赞数')
    count = models.IntegerField(default=0, verbose_name='浏览量')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章表'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论用户')
    date = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    content = models.CharField(max_length=140, verbose_name="回复内容")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='评论文章')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=True, verbose_name='被评论用户')

    def __str__(self):
        return self.author.nickname

    class Meta:
        verbose_name_plural = '评论表'
