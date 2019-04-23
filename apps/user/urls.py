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
from django.urls import path

from apps.user import views

urlpatterns = [
    # 注册
    path('sign_up/', views.sign_up, name='sign_up'),
    # 登陆
    path('sign_in/', views.sign_in, name='sign_in'),
    # 注销
    path('sign_out/', views.sign_out, name='sign_out'),
    # 用户中心
    path('user/<int:uid>/', views.user, name='user'),
    # 用户修改密码
    path('repwd/<int:uid>/', views.repwd, name='repwd'),
    # 用户评论记录
    path('comment/<int:uid>/', views.comment, name='comment'),
    # 用户删除评论记录
    path('comment_del/<int:cid>/', views.comment_del, name='comment_del'),
    # 用户收藏记录
    path('articlecol/<int:uid>/', views.articlecol, name='articlecol'),
    # 用户删除收藏记录
    path('articlecol_del/<int:cid>/', views.articlecol_del, name='articlecol_del'),
]
