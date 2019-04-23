from django.contrib import admin

from user.models import *

# 此处设置页面头部标题
admin.site.site_title = '新码农站点后台'
# 此处设置页面显示标题
admin.site.site_header = '新码农后台管理系统'


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'nickname', 'birthday', 'gender', 'photo', 'phone', 'email', 'desc',
                    'addtime']
    # list_display_links 设置其他字段也可以点击链接进入编辑界面
    list_display_links = ['id', 'username']
    list_per_page = 50
    list_filter = ['gender', 'birthday']
    search_fields = ['username', 'nickname', 'phone']
    # list_editable 设置默认可编辑字段
    list_editable = ['nickname', 'birthday', 'gender', 'phone', 'email', 'desc']
    ordering = ['-addtime']
    # date_hierarchy 详细时间分层筛选　
    date_hierarchy = 'addtime'


@admin.register(Leavemsg)
class Leavemsgadmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'user', 'addtime']
    # list_display_links 设置其他字段也可以点击链接进入编辑界面
    list_display_links = ['id', 'user']
    list_per_page = 50
    list_filter = ['user']
    search_fields = ['user']
    # list_editable 设置默认可编辑字段
    list_editable = ['content']
    ordering = ['-addtime']
    # date_hierarchy 详细时间分层筛选　
    date_hierarchy = 'addtime'
