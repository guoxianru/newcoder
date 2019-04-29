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
from django.urls import path
from blog import views

urlpatterns = [
    # 首页加载更多
    path("more/<int:pagenum>/", views.more),
    # 注册
    path('signup/', views.signup),
    # 登陆
    path('login/', views.login),
    # 注销
    path('logout/', views.logout),
    # 关于我
    path('myblurb/', views.myblurb),
    # 用户信息
    path('userinfo/<int:id>/', views.userinfo),
    # 分类列表
    path('typelist/<int:tid>/', views.typelist),
    path('typelist/<int:tid>/<int:num>/', views.typelist),
    # 添加文章
    path('addarticle/', views.addarticle),
    # 文章详情
    path('article/<int:id>/', views.article),
    # 点赞
    path('likes/<int:id>/', views.likes),
    # 评论
    path("comment/<int:id>/", views.comment),
    path("comment/<int:id>/<int:pid>/", views.comment),
    # 三级联动
    path("city/",views.city),
    path('city/<int:pid>/',views.city2)
]
