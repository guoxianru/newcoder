# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from blog.models import *


def recommend(request):
    # 侧边栏文章
    # 特别推荐，显示前3
    articles_2 = Article.objects.filter(is_recommend=2)[:3]
    # 推荐文章，显示前5
    articles_1 = Article.objects.filter(is_recommend=1)[:5]
    # 推荐文章第一位
    if articles_1.count() > 0:
        articles_1_1 = articles_1[0]
        articles_1 = articles_1[1:5]
    else:
        articles_1_1 = []
        articles_1 = articles_1[1:5]
    # 点击排行，显示前5
    articles_count = Article.objects.order_by('-count')[:5]
    # 点击排行第一位
    if articles_count.count() > 0:
        articles_count_1 = articles_count[0]
        articles_count = articles_count[1:5]
    else:
        articles_count_1 = []
        articles_count = articles_count[1:5]
    # 标签云，显示前20
    tags = Tag.objects.all()[:20]
    # 侧边栏文章

    content = {
        # 特别推荐，显示前3
        'articles_2': articles_2,
        # 推荐文章，显示前5
        'articles_1': articles_1,
        # 推荐文章第一位
        'articles_1_1': articles_1_1,
        # 点击排行，显示前5
        'articles_count': articles_count,
        # 点击排行第一位
        'articles_count_1': articles_count_1,
        # 标签云，显示前20
        'tags': tags
    }
    return content
