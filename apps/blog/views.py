from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q

from blog.models import *
from user.models import *

pagesize = 13


# 验证登陆装饰器
def user_login_req(func):
    def inner(request, *args, **kwargs):
        obj = request.session.get('user_id')
        if obj:
            # 已经登录
            return func(request, *args, **kwargs)
        else:
            # 没有登录
            # 判断发送的请求是不是ajax
            # 如果是ajax，则返回一个redirect字符串
            # 表示是一个ajax请求
            if 'XMLHttpRequest' == request.META.get('HTTP_X_REQUESTED_WITH'):
                return HttpResponse('请登录')
            else:
                # 不是ajax请求，是浏览器发送的请求，正常返回登录
                messages.success(request, "请先登录！！！")
                return redirect('/user/sign_in/')

    return inner


# 微信验证
def weixin_auth(request):
    return HttpResponse('hC03z28vx2ij7bpL')


# 首页
def index(request):
    # 默认按时间排序，显示前20
    articles = Article.objects.order_by('-addtime')[:pagesize]
    # 首页轮播，显示前5
    articles_plant = Article.objects.filter(is_plant=1)[:5]
    # 首页置顶，显示前2
    articles_top = Article.objects.filter(is_top=1)[:2]
    return render(request, 'blog/index.html', locals())


# 首页加载更多
def more(request, pagenum):
    articles = Article.objects.order_by("-addtime")[pagenum * pagesize:(pagenum + 1) * pagesize]
    # 判断当前获取的分页是否为空
    if len(articles) > 0:
        # 不为空在做操作,渲染页面
        return render(request, "blog/index_item.html", locals())
    elif len(articles) == 0:
        # 为空返回‘empty’给js
        return HttpResponse("empty")


# 文章列表
def article_list(request, key, tid, num=1):
    if key == 'type':
        word = 'type'
        # 通过分类筛选文章
        articles = Article.objects.filter(type=tid).order_by('-addtime')
        # 根据分类获取类型信息
        type_detail = Type.objects.filter(id=tid).first()
        # 分类ID
        name_id = type_detail.id
        # 分类名称
        name_name = type_detail.typename
        # 分类简介
        name_label = type_detail.label
    else:
        word = 'tag'
        # 通过标签筛选文章
        articles = Article.objects.filter(tag=tid).order_by('-addtime')
        # 根据标签获取类型信息
        tag_detail = Tag.objects.filter(id=tid).first()
        # 标签ID
        name_id = tag_detail.id
        # 标签名称
        name_name = tag_detail.tagname
        # 标签简介
        name_label = tag_detail.label
    # 生成分页器
    p = Paginator(articles, 20)
    page = p.get_page(num)
    # 页码范围
    prange = p.page_range
    return render(request, 'blog/level1_article_list.html', locals())


# 文章详情
def article_detail(request, aid):
    # 根据文章id获取文章信息
    article = Article.objects.filter(id=aid).first()
    # 本篇文章所有标签
    all_tag = article.tag.all()
    # 获取本篇文章的上一篇
    prev_aid = aid - 1
    prev_article = Article.objects.filter(id=prev_aid).first()
    # 获取本篇文章的上一篇
    next_aid = aid + 1
    next_article = Article.objects.filter(id=next_aid).first()
    # 根据文章标签获取相关文章信息
    relevant_article = []
    for i in all_tag:
        article_tag = Article.objects.filter(tag=i.id)
        relevant_article += article_tag
    if len(relevant_article) > 10:
        relevant_article = set(relevant_article[:10])
    # 根据父级字段是否有值来筛选出直接评论文章的评论
    comments = article.comment_set.filter(parent=None).order_by("-addtime")
    # 文章浏览量+1
    id = request.session.get('user_id')
    ids = request.session.get('ids')
    if id:
        if ids:
            if id in ids:
                pass
            else:
                # 加一操作
                article.count += 1
                ids.append(id)
            # 把新的ids写入到session中
            request.session['ids'] = ids
        else:
            ids = []
            ids.append(id)
            request.session['ids'] = ids
            # 加一操作
            article.count += 1
    else:
        pass
    article.save()
    # 获取本文章所有评论
    comments = Comment.objects.filter(article=aid).order_by('-addtime')
    comment_num = len(comments)
    return render(request, 'blog/level2_article_detail.html', locals())


# 点赞
@user_login_req
def like(request, id):
    art = Article.objects.get(id=id)
    ids = request.session.get('ids')
    # 在一个会话session中,记录下收藏、点赞的文章id,已经点过一次再点,我们认为是取消这个操作
    if ids:
        if id in ids:
            # 减一操作
            art.like = art.like - 1
            ids.remove(id)
        else:
            # 加一操作
            art.like = art.like + 1
            ids.append(id)
        # 把新的ids写入到session中
        request.session['ids'] = ids
    else:
        ids = []
        ids.append(id)
        request.session['ids'] = ids
        # 加一操作
        art.like = art.like + 1
    art.save()
    # 返回我们最新的点赞次数
    return HttpResponse(str(art.like))


# 评论
@user_login_req
def comment(request, aid, pid=0):
    # 从session中去拿登录用户的id
    uid = request.session.get("user_id")
    # 把一个文章评论插入到数据库中
    user = User.objects.get(id=uid)
    article = Article.objects.get(id=aid)
    content = request.POST.get("content", '')
    if content == '':
        messages.success(request, "评论不能为空")
        return redirect("/blog/article_detail/{}/".format(aid))
    if pid:
        # 根据model多了一个父评论字段,我们这里也要增加一个新字段
        parent = Comment.objects.get(id=pid)
    else:
        parent = None
    # 把数据保存到数据表中
    Comment.objects.create(user=user, article=article, content=content, parent=parent)
    return redirect("/blog/article_detail/{}/".format(aid))


# 收藏
@user_login_req
def article_col(request, aid):
    uid = request.session.get("user_id")
    user = User.objects.get(id=uid)
    article = Article.objects.get(id=aid)
    col = Articlecol.objects.filter(user=user, article=article).count()
    # 判断当前文章是否收藏
    if col == 0:
        Articlecol.objects.create(user=user, article=article)
        return HttpResponse("1")
    else:
        return HttpResponse("0")


# 时间轴
def time_axis(request):
    articles = Article.objects.order_by('-addtime')
    return render(request, 'blog/level1_time_axis.html', locals())


# 关于我
def about_me(request):
    return render(request, 'blog/level1_about_me.html', locals())


# 留言
def leave_msg(request):
    msgs = Leavemsg.objects.all().order_by('-addtime')
    msg_num = len(msgs)
    if request.method == "GET":
        return render(request, 'blog/level1_leave_msg.html', locals())
    if request.method == 'POST':
        uid = request.session.get("user_id")
        user = User.objects.get(id=uid)
        content = request.POST.get("content", '')
        if content == '':
            messages.success(request, "留言不能为空")
            return redirect("/blog/leave_msg/")
        Leavemsg.objects.create(user=user, content=content)
        return redirect("/blog/leave_msg/")


# 搜索
@user_login_req
def search(request):
    keyword = request.POST.get('keyboard', '')
    articles = Article.objects.filter(Q(title__icontains=keyword) | Q(author__nickname__icontains=keyword))
    articles_num = len(articles)
    return render(request, 'blog/level3_search.html', locals())
