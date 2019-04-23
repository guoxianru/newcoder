"""newcoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 导入静态文件模块
from django.views.static import serve
# 导入配置文件里的文件上传配置
from django.conf import settings

from apps.blog import views

urlpatterns = [
    # 后台
    path('admin/', admin.site.urls),
    # 应用
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    # 首页
    path('', views.index),
    # 微信验证
    path('MP_verify_hC03z28vx2ij7bpL.txt', views.weixin_auth),
    # 配置富文本的URL
    path('summernote/', include('django_summernote.urls')),
    # 用于上传图片文件
    path('static/', serve, {'document_root': settings.MEDIA_ROOT}),
    # 用于加载静态文件
    path('static/', serve, {'document_root': settings.STATIC_ROOT}),
]
