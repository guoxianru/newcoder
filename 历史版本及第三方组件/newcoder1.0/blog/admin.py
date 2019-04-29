from django.contrib import admin
from .models import *

# 此处设置页面头部标题
admin.site.site_title = '新码农站点后台'
# 此处设置页面显示标题
admin.site.site_header = '新码农后台管理系统'


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'nickname', 'password', 'photo', 'phone', 'email', 'desc', 'date']
    # list_display_links 设置其他字段也可以点击链接进入编辑界面
    list_display_links = ['id', 'username']
    list_per_page = 10
    list_filter = ['username', 'nickname']
    search_fields = ['username', 'nickname']
    # list_editable 设置默认可编辑字段
    list_editable = ['nickname']
    ordering = ['-date']
    # date_hierarchy 详细时间分层筛选　
    date_hierarchy = 'date'


@admin.register(Type)
class Typeadmin(admin.ModelAdmin):
    list_display = ['id', 'typename']
    list_per_page = 10
    list_filter = ['typename']
    search_fields = ['typename']
    # list_editable 设置默认可编辑字段
    list_editable = ['typename']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'type', 'date', 'pic', 'like', 'count']
    # list_display_links 设置其他字段也可以点击链接进入编辑界面
    list_display_links = ['id', 'title']
    list_per_page = 10
    list_filter = ['title', 'author', 'type']
    search_fields = ['title', 'author', 'type']
    # list_editable 设置默认可编辑字段
    list_editable = ['type']
    ordering = ['-date']
    # date_hierarchy 详细时间分层筛选　
    date_hierarchy = 'date'


@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'date', 'content', 'article', 'parent']
    # list_display_links 设置其他字段也可以点击链接进入编辑界面
    list_display_links = ['id', 'author']
    list_per_page = 10
    list_filter = ['author', 'article']
    search_fields = ['author', 'article']
    # list_editable 设置默认可编辑字段
    list_editable = ['content']
    ordering = ['-date']
    # date_hierarchy 详细时间分层筛选　
    date_hierarchy = 'date'
