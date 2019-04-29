"""newcoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a.css URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a.css URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a.css URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# 导入静态文件模块
from django.views.static import serve
# 导入配置文件里的文件上传配置
from django.conf import settings
from blog import views

urlpatterns = [
    # 后台
    path('admin/', admin.site.urls),
    # 应用
    path('blog/', include('blog.urls')),
    # 首页
    path('', views.index),
    # 配置DjangoUeditor富文本的URL
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path('^static/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  # 增加此行
]
