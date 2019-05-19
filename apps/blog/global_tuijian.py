# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from blog.models import *


def recommend(request):
    # 心情随笔
    type_1 = Type.objects.get(id=1)
    tags_1 = Tag.objects.filter(type_id=1).order_by('-addtime')[:5]
    # 时事点评
    type_2 = Type.objects.get(id=2)
    tags_2 = Tag.objects.filter(type_id=2).order_by('-addtime')[:5]
    # 技术分享
    type_3 = Type.objects.get(id=3)
    tags_3 = Tag.objects.filter(type_id=3).order_by('-addtime')[:5]
    # 所有打赏
    rewards = Reward.objects.all().order_by('-money')[:10]
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
    tags = Tag.objects.all()

    # 以键值对形式传递参数
    content = {
        # 心情随笔
        'type_1': type_1,
        'tags_1': tags_1,
        # 时事点评
        'type_2': type_2,
        'tags_2': tags_2,
        # 技术分享
        'type_3': type_3,
        'tags_3': tags_3,
        # 所有打赏
        'rewards': rewards,
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
        # 标签云，显示所有标签
        'tags': tags
    }
    return content
