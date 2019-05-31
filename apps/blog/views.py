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
def article_list(request, key, unique_id, num=1):
    if key == 'type':
        word = 'type'
        # 根据分类获取类型信息
        type_detail = Type.objects.filter(unique_id=unique_id).first()
        # 分类ID
        name_id = type_detail.unique_id
        # 分类名称
        name_name = type_detail.typename
        # 分类简介
        name_label = type_detail.label
        # 通过分类筛选文章
        articles = Article.objects.filter(type=type_detail).order_by('-addtime')
    else:
        word = 'tag'
        # 根据标签获取类型信息
        tag_detail = Tag.objects.filter(unique_id=unique_id).first()
        # 标签ID
        name_id = tag_detail.unique_id
        # 标签名称
        name_name = tag_detail.tagname
        # 标签简介
        name_label = tag_detail.label
        # 通过标签筛选文章
        articles = Article.objects.filter(tag=tag_detail).order_by('-addtime')
    # 生成分页器
    p = Paginator(articles, 13)
    # 当前页
    page = p.get_page(num)
    # 当前页左边连续的页码号，初始值为空
    left = []
    # 当前页右边连续的页码号，初始值为空
    right = []
    # 标示第 1 页页码后是否需要显示省略号
    left_has_more = False
    # 标示最后一页页码前是否需要显示省略号
    right_has_more = False
    # 标示是否需要显示第 1 页的页码号
    first = False
    # 标示是否需要显示最后一页的页码号
    last = False
    # 获得用户当前请求的页码号
    page_number = page.number
    # 获得分页后的总页数
    total_pages = p.num_pages
    # 获得整个分页页码列表
    page_range = p.page_range
    # 根据当前页码进行判断
    if page_number == 1:
        # 如果用户请求的是第一页的数据，那么当前页左边的不需要数据，因此 left=[]（已默认为空）
        # 此时只要获取当前页右边的连续页码号
        # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 right = [2, 3]
        # 注意这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码
        right = page_range[page_number:page_number + 2]
        if len(right) == 0:
            right = [1]
        # 如果最右边的页码号比最后一页的页码号减去 1 还要小
        # 说明最右边的页码号和最后一页的页码号之间还有其它页码，因此需要显示省略号，通过 right_has_more 来指示
        if right[-1] < total_pages - 1:
            right_has_more = True
        # 如果最右边的页码号比最后一页的页码号小，说明当前页右边的连续页码号中不包含最后一页的页码
        # 所以需要显示最后一页的页码号，通过 last 来指示
        if right[-1] < total_pages:
            last = True
    elif page_number == total_pages:
        # 如果用户请求的是最后一页的数据，那么当前页右边就不需要数据，因此 right=[]（已默认为空）
        # 此时只要获取当前页左边的连续页码号
        # 比如分页页码列表是 [1, 2, 3, 4]，那么获取的就是 left = [2, 3]
        # 这里只获取了当前页码后连续两个页码，你可以更改这个数字以获取更多页码
        left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
        # 如果最左边的页码号比第 2 页页码号还大
        # 说明最左边的页码号和第 1 页的页码号之间还有其它页码，因此需要显示省略号，通过 left_has_more 来指示
        if left[0] > 2:
            left_has_more = True
        # 如果最左边的页码号比第 1 页的页码号大，说明当前页左边的连续页码号中不包含第一页的页码
        # 所以需要显示第一页的页码号，通过 first 来指示
        if left[0] > 1:
            first = True
    else:
        # 用户请求的既不是最后一页，也不是第 1 页，则需要获取当前页左右两边的连续页码号
        # 这里只获取了当前页码前后连续两个页码，你可以更改这个数字以获取更多页码
        left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
        right = page_range[page_number:page_number + 2]
        # 是否需要显示最后一页和最后一页前的省略号
        if right[-1] < total_pages - 1:
            right_has_more = True
        if right[-1] < total_pages:
            last = True
        # 是否需要显示第 1 页和第 1 页后的省略号
        if left[0] > 2:
            left_has_more = True
        if left[0] > 1:
            first = True
    return render(request, 'blog/level1_article_list.html', locals())


# 文章详情
def article_detail(request, unique_id):
    # 根据文章id获取文章信息
    article = Article.objects.filter(unique_id=unique_id).first()
    aid = article.id
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
    comments = Comment.objects.filter(article=aid, parent=None).order_by('-addtime')
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
def comment(request, unique_id, pid=0):
    # 从session中去拿登录用户的id
    uid = request.session.get("user_id")
    # 把一个文章评论插入到数据库中
    user = User.objects.get(unique_id=uid)
    article = Article.objects.get(unique_id=unique_id)
    content = request.POST.get("content", '')
    if content == '':
        messages.success(request, "评论不能为空")
        return redirect("/blog/article_detail/{}/".format(unique_id))
    if pid:
        # 根据model多了一个父评论字段,我们这里也要增加一个新字段
        parent = Comment.objects.get(id=pid)
    else:
        parent = None
    # 把数据保存到数据表中
    Comment.objects.create(user=user, article=article, content=content, parent=parent, unique_id=NewUUID().random(8))
    return redirect("/blog/article_detail/{}/".format(unique_id))


# 收藏
@user_login_req
def article_col(request, aid):
    uid = request.session.get("user_id")
    user = User.objects.get(unique_id=uid)
    article = Article.objects.get(id=aid)
    col = Articlecol.objects.filter(user=user, article=article).count()
    # 判断当前文章是否收藏
    if col == 0:
        Articlecol.objects.create(user=user, article=article, unique_id=NewUUID().random(8))
        return HttpResponse("1")
    else:
        return HttpResponse("0")


# 时间轴
def time_axis(request):
    article_time = Article.objects.all().order_by('-addtime')
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
        user = User.objects.get(unique_id=uid)
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
    if keyword == '':
        messages.success(request, "搜索关键词不能为空")
        return redirect("/")
    articles = Article.objects.filter(Q(title__icontains=keyword) | Q(author__nickname__icontains=keyword))
    articles_num = len(articles)
    return render(request, 'blog/level3_search.html', locals())


# 作者信息
@user_login_req
def author_info(request, unique_id):
    author = User.objects.get(unique_id=unique_id)
    return render(request, 'blog/level4_author_info.html', locals())
