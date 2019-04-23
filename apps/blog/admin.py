from django.contrib import admin

from blog.models import *

# 此处设置页面头部标题
admin.site.site_title = '新码农站点后台'
# 此处设置页面显示标题
admin.site.site_header = '新码农后台管理系统'


@admin.register(Type)
class Typeadmin(admin.ModelAdmin):
    list_display = ['id', 'typename', 'label', 'addtime']
    list_per_page = 50
    list_filter = ['typename']
    search_fields = ['typename']
    # list_editable 设置默认可编辑字段
    list_editable = ['typename', 'label']
    ordering = ['-addtime']
    # date_hierarchy 详细时间分层筛选　
    date_hierarchy = 'addtime'


@admin.register(Tag)
class Tagadmin(admin.ModelAdmin):
    list_display = ['id', 'tagname', 'label', 'addtime']
    list_per_page = 50
    list_filter = ['tagname']
    search_fields = ['tagname']
    # list_editable 设置默认可编辑字段
    list_editable = ['tagname', 'label']
    ordering = ['-addtime']
    # date_hierarchy 详细时间分层筛选　
    date_hierarchy = 'addtime'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'type', 'addtime', 'pic', 'like', 'count', 'is_plant', 'is_top',
                    'is_recommend']
    filter_horizontal = ('tag',)
    # list_display_links 设置其他字段也可以点击链接进入编辑界面
    list_display_links = ['id', 'title']
    list_per_page = 50
    list_filter = ['title', 'author', 'type', 'tag']
    search_fields = ['title', 'author', 'type', 'tag']
    # list_editable 设置默认可编辑字段
    list_editable = ['type', 'like', 'count', 'is_plant', 'is_top', 'is_recommend']
    ordering = ['-addtime']
    # date_hierarchy 详细时间分层筛选　
    date_hierarchy = 'addtime'


@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'user', 'article', 'addtime', 'parent']
    # list_display_links 设置其他字段也可以点击链接进入编辑界面
    list_display_links = ['id', 'user']
    list_per_page = 50
    list_filter = ['user', 'article']
    search_fields = ['user', 'article']
    # list_editable 设置默认可编辑字段
    list_editable = ['content']
    ordering = ['-addtime']
    # date_hierarchy 详细时间分层筛选　
    date_hierarchy = 'addtime'


@admin.register(Articlecol)
class Articlecoladmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'user', 'addtime']
    # list_display_links 设置其他字段也可以点击链接进入编辑界面
    list_display_links = ['id', 'user']
    list_per_page = 50
    list_filter = ['user', 'article']
    search_fields = ['user', 'article']
    # list_editable 设置默认可编辑字段
    list_editable = ['article']
    ordering = ['-addtime']
    # date_hierarchy 详细时间分层筛选　
    date_hierarchy = 'addtime'
