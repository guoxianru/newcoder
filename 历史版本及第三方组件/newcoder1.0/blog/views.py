from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import *
from .forms import *
from . import utils
from . import decorators
from django.forms import forms
from DjangoUeditor.forms import UEditorField

pagesize = 5


class DjangoUeditorForm(forms.Form):
    content = UEditorField('', width=800, height=500, toolbars="full", imagePath="imgs/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000}, settings={})


# 首页
def index(request):
    list = Article.objects.order_by('-date')[0:pagesize]  # 数据切片，显示[0:5]
    hotlist = Article.objects.order_by('-count')[0:10]
    return render(request, 'index.html', locals())


# 首页加载更多
def more(request, pagenum):
    list = Article.objects.order_by("-date")[pagenum * pagesize:(pagenum + 1) * pagesize]
    # 判断当前获取的分页是否为空
    if len(list) > 0:
        # 不为空在做操作,渲染页面
        return render(request, "index_item.html", locals())
    elif len(list) == 0:
        # 为空返回‘empty’给js
        return HttpResponse("empty")


# 注册
def signup(request):
    if request.method == "GET":
        return render(request, 'level0_signup.html', locals())
    if request.method == 'POST':
        f = SignupForm(request.POST, request.FILES)
        if f.is_valid():
            count = User.objects.filter(username=f.cleaned_data["username"]).count()
            if count > 0:
                return render(request, 'level0_signup.html', {'msg': '用户名已经存在', 'data': f.data})
            if f.data['password'] == f.data['password1']:
                cleandata = f.cleaned_data
                cleandata['password'] = utils.encryption(cleandata['password'])
                User.objects.create(**cleandata)
                return redirect("/blog/login/")
            else:
                return render(request, 'level0_signup.html', {'msg': '两次密码不一样', 'data': f.data})
        else:
            return render(request, 'level0_signup.html', {'errors': f.errors, 'data': f.data})


# 登陆
def login(request):
    if request.method == 'GET':
        username = ''
        if request.session.get('save'):
            username = request.session.get('username')
        return render(request, "level0_login.html", locals())
    elif request.method == 'POST':
        username = request.POST.get("username")
        save = request.POST.get("save")
        f = LoginForm(request.POST)
        if f.is_valid():
            users = User.objects.filter(username=f.cleaned_data['username'],
                                        password=utils.encryption(f.cleaned_data['password']))
            if len(users) > 0:
                request.session['user_id'] = users[0].id
                request.session['user_username'] = users[0].username
                request.session['user_photo'] = users[0].photo.name
                request.session['save'] = 0
                request.session['username'] = username
                response = redirect("/")
                if save:
                    response.set_cookie('name', username)
                    request.session['save'] = 1
                return response
            else:
                return render(request, 'level0_login.html', {'msg': '用户名或密码错误', 'data': f.data})
        else:
            return render(request, "level0_login.html", {"errors": f.errors, "data": f.data})


# 注销
def logout(request):
    # 清空session存储的数据
    request.session.flush()
    return redirect('/')


# 关于我
def myblurb(request):
    return render(request, 'level1_myblurb.html', locals())


# 用户信息
def userinfo(request, id):
    user = User.objects.get(id=id)
    return render(request, 'level1_userinfo.html', locals())


# 分类列表
def typelist(request, tid, num=1):
    list = Article.objects.filter(type=tid)  # 通过类型id筛选文章
    typename = list[0].type.typename  # 类型名称
    p = Paginator(list, 5)  # 生成分页器
    page = p.get_page(num)
    prange = p.page_range  # 页码范围
    return render(request, 'level2_typelist.html', locals())


# 添加文章
def addarticle(request):
    types = Type.objects.all()  # 文章类型
    form = DjangoUeditorForm()
    if request.method == "GET":
        return render(request, 'level3_addarticle.html', locals())
    else:
        f = AddarticleForm(request.POST, request.FILES)
        if f.is_valid():
            uid = request.session["user_id"]
            author = User.objects.get(id=uid)
            tid = f.cleaned_data["type"]
            type = Type.objects.get(id=tid)
            cleandata = f.cleaned_data
            cleandata['type'] = type
            cleandata['author'] = author
            Article.objects.create(**cleandata)

            return redirect("/")  # 添加成功，重定向首页
        else:
            return render(request, 'level3_addarticle.html', {"errors": f.errors, "data": f.data, 'form': form})


# 文章详情
def article(request, id):
    article = Article.objects.filter(id=id)[0]  # 根据文章id获取文章信息
    count = Article.objects.filter(author=article.author).count()  # 获取该作者文章总数
    title = Article.objects.filter(author=article.author).order_by("-date")[0].title  # 获取该作者最近文章标题
    tid = Article.objects.filter(author=article.author).order_by("-date")[0].id  # 获取该作者最近文章ID
    comments = article.comment_set.filter(parent=None).order_by("-date")  # 根据父级字段是否有值来筛选出直接评论文章的评论
    article.count = article.count + 1  # 文章浏览量+1
    article.save()
    return render(request, 'level3_article.html', locals())


@decorators.check
# 点赞
def likes(request, id):
    art = Article.objects.get(id=id)
    ids = request.session.get('ids')
    # 在一个回话session中,记录下收藏、点赞的文章id,已经点过一次再点,我们认为是取消这个操作
    if ids:
        if id in ids:
            art.like = art.like - 1  # 减一操作
            ids.remove(id)
        else:
            art.like = art.like + 1  # 加一操作
            ids.append(id)
        request.session['ids'] = ids  # 把新的ids写入到session中
    else:
        ids = []
        ids.append(id)
        request.session['ids'] = ids
        art.like = art.like + 1  # 加一操作
    art.save()
    return HttpResponse(str(art.like))  # 返回我们最新的点赞次数


@decorators.check
# 评论
def comment(request, id, pid=0):
    # 从session中去拿登录用户的id
    uid = request.session.get("user_id")
    # 把一个文章评论插入到数据库中
    author = User.objects.get(id=uid)
    article = Article.objects.get(id=id)
    content = request.POST.get("content")
    if pid:
        parent = Comment.objects.get(id=pid)  # 根据model多了一个父评论字段,我们这里也要增加一个新字段
    else:
        parent = None
    # 把数据保存到数据表中
    Comment.objects.create(author=author, article=article, content=content, parent=parent)
    return redirect("/blog/article/{}/".format(id))


# 三级联动
def city(request):
    pass


# 三级联动
def city2(request, pid):
    pass
