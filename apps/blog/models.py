from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django_summernote.fields import SummernoteTextField

User = get_user_model()


# 文章分类表
class Type(models.Model):
    typename = models.CharField(max_length=20, unique=True, verbose_name='分类名称')
    label = models.CharField(max_length=255, verbose_name='分类简介')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        # 指定在admin管理界面中显示中文,表示单数形式的显示
        verbose_name = '文章分类表'
        # 指定在admin管理界面中显示中文,表示复数形式的显示
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.typename


'''
心情随笔 - 求人不如求己，真正能够解忧的，只有自己。
时事点评 - 如果你曾歌颂黎明，那么也请你拥抱黑夜。
技术分享 - 合抱之木，生于毫末；九层之台，起于垒土；千里之行，始于足下。
'''


# 文章标签表
class Tag(models.Model):
    tagname = models.CharField(max_length=20, unique=True, verbose_name='标签名称')
    label = models.CharField(max_length=255, verbose_name='标签简介')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '文章标签表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tagname


'''
随手记 - 记录生活点点滴滴。
人生感悟 - 人只要不失去方向，就不会失去自己。
Python - Python，绵薄技术，与君共勉。
Ubuntu - Ubuntu，绵薄技术，与君共勉。
MySQL - MySQL，绵薄技术，与君共勉。
'''


# 文章表
class Article(models.Model):
    title = models.CharField(max_length=40, unique=True, verbose_name='文章标题')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章作者')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='文章分类')
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    pic = models.ImageField(upload_to="blog/pics", null=True, blank=True, verbose_name='文章配图')
    label = models.CharField(max_length=255, null=True, blank=True, verbose_name='文章简介')
    content = SummernoteTextField()
    like = models.IntegerField(default=0, verbose_name='点赞数')
    count = models.IntegerField(default=0, verbose_name='浏览量')
    # 0为不轮播，1为轮播
    is_plant = models.IntegerField(default=0, verbose_name='是否轮播')
    # 0为不置顶，1为置顶
    is_top = models.IntegerField(default=0, verbose_name='是否置顶')
    # 0为不推荐，1为推荐，2特别推荐
    is_recommend = models.IntegerField(default=0, verbose_name='是否推荐')

    class Meta:
        verbose_name = '文章表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 文章评论表
class Comment(models.Model):
    content = models.CharField(max_length=140, verbose_name="回复内容")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论用户')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='评论文章')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=True, verbose_name='被评论用户')

    class Meta:
        verbose_name = '文章评论表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nickname


# 文章收藏表
class Articlecol(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='所属文章')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='所属会员')
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '文章收藏表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.nickname


# 微信开发
class WxToken(models.Model):
    token = models.CharField(max_length=200)
    lifetime = models.DateTimeField(default=0)

    def get_date(self):
        delta = timezone.now() - self.lifetime
        if delta.seconds < 6000:
            return True
        else:
            return False


# 微信开发
class JsToken(models.Model):
    token = models.CharField(max_length=200)
    lifetime = models.DateTimeField(default=0)

    def get_date(self):
        delta = timezone.now() - self.lifetime
        if delta.seconds < 6000:
            return True
        else:
            return False


# 打赏表
class Reward(models.Model):
    name = models.CharField(max_length=20)
    money = models.FloatField(default=0.0)
    addtime = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '打赏表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
