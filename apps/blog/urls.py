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

from apps.blog import views

urlpatterns = [
    # 首页加载更多
    path("more/<int:pagenum>/", views.more, name='more'),
    # 文章列表
    path('article_list/<str:key>/<int:tid>/', views.article_list, name='article_list'),
    path('article_list/<str:key>/<int:tid>/<int:num>/', views.article_list, name='article_list'),
    # 文章详情
    path('article_detail/<int:aid>/', views.article_detail, name='article_detail'),
    # 时间轴
    path('time_axis/', views.time_axis, name='time_axis'),
    # 关于我
    path('about_me/', views.about_me, name='about_me'),
    # 留言
    path('leave_msg/', views.leave_msg, name='leave_msg'),
    # 点赞
    path('like/<int:id>/', views.like, name='like'),
    # 评论
    path("comment/<int:aid>/", views.comment, name='comment'),
    path("comment/<int:aid>/<int:pid>/", views.comment, name='comment'),
    # 收藏
    path("article_col/<int:aid>/", views.article_col, name='article_col'),
    # 留言
    path("leave_msg/", views.leave_msg, name='leave_msg'),
    # 留言
    path("search/", views.search, name='search'),
]
