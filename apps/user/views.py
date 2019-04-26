import re

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.db.models.query_utils import Q
from django.contrib import messages

from user.models import *
from blog.models import *
from user.forms import SignupForm, LoginForm


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


# 验证当前用户权限装饰器
def user_auth_req(func):
    def auth(request, *args, **kwargs):
        user_session = request.session.get('user_id')
        user_info = re.findall(r'/(\d)/', request.path_info)[0]
        if int(user_session) == int(user_info):
            return func(request, *args, **kwargs)
        else:
            messages.success(request, '没有访问当前页面权限！！！')
            return redirect("/user/user/{}/".format(user_session))

    return auth


# 注册
def sign_up(request):
    if request.method == "GET":
        return render(request, 'user/level0_sign_up.html', locals())
    if request.method == 'POST':
        f = SignupForm(request.POST, request.FILES)
        if f.is_valid():
            count = User.objects.filter(username=f.cleaned_data["username"]).count()
            if count > 0:
                return render(request, 'user/level0_sign_up.html', {'msg': '用户名已经存在', 'data': f.data})
            count1 = User.objects.filter(nickname=f.cleaned_data["nickname"]).count()
            if count1 > 0:
                return render(request, 'user/level0_sign_up.html', {'msg': '昵称已经存在', 'data': f.data})
            if f.data['password'] != f.data['password1']:
                return render(request, 'user/level0_sign_up.html', {'msg': '两次密码不一样', 'data': f.data})
            cleandata = f.cleaned_data
            cleandata['password'] = make_password(cleandata['password'])
            User.objects.create(**cleandata)
            messages.success(request, '注册成功')
            return redirect("/user/sign_in/")
        else:
            return render(request, 'user/level0_sign_up.html', {'errors': f.errors, 'data': f.data})


# 登陆
def sign_in(request):
    if request.method == 'GET':
        next = request.GET.get('next', '')
        username = ''
        if request.session.get('save'):
            username = request.COOKIES.get('username')
        return render(request, "user/level0_sign_in.html", locals())
    if request.method == 'POST':
        username = request.POST.get("username")
        save = request.POST.get("save")
        f = LoginForm(request.POST)
        next = request.POST.get('next', '')
        if f.is_valid():
            user = User.objects.filter(
                Q(username=f.cleaned_data['username']) | Q(phone=f.cleaned_data['username'])).first()
            if user:
                if check_password(f.cleaned_data['password'], user.password):
                    request.session['user_id'] = user.id
                    request.session['user_username'] = user.nickname
                    request.session['user_photo'] = user.photo.name
                    request.session['save'] = 0
                    if next == '':
                        response = redirect('/')
                    else:
                        response = redirect(next)
                    response.set_cookie('username', user.username, 3600)
                    if save:
                        request.session['save'] = 1
                    return response
                else:
                    return render(request, 'user/level0_sign_in.html', {'msg': '用户名或密码错误', 'data': f.data})
            else:
                return render(request, 'user/level0_sign_in.html', {'msg': '用户名不存在', 'data': f.data})
        else:
            return render(request, "user/level0_sign_in.html", {"errors": f.errors, "data": f.data})
    return render(request, "user/level0_sign_in.html", locals())


# 注销
@user_login_req
def sign_out(request):
    # 清空session存储的数据
    request.session.flush()
    response = redirect('/')
    response.delete_cookie('username')
    return redirect('/')


# 用户中心
@user_login_req
@user_auth_req
def user(request, uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST':
        # 昵称修改
        nickname = request.POST.get('nickname', '')
        if nickname == user.nickname:
            pass
        else:
            if User.objects.filter(nickname=nickname).count() > 0:
                messages.success(request, '昵称已被使用')
                return redirect("/user/user/{}/".format(uid))
            else:
                user.nickname = nickname
                user.save()
        # 生日修改
        birthday = request.POST.get('birthday', '')
        if birthday == user.birthday:
            pass
        else:
            user.birthday = birthday
            user.save()
        # 性别修改
        gender = request.POST.get('gender', '')
        if gender == user.gender:
            pass
        else:
            user.gender = gender
            user.save()
        # 头像修改
        photo = request.FILES.get('photo', '')
        if photo:
            if ('user/photo/' + photo.name) == user.photo.name:
                pass
            else:
                User.objects.update_or_create({"photo": photo}, id=uid)
        else:
            pass
        # 手机号修改
        phone = request.POST.get('phone', '')
        if phone == user.phone:
            pass
        else:
            if User.objects.filter(phone=phone).count() > 0:
                messages.success(request, '手机号已被使用')
                return redirect("/user/user/{}/".format(uid))
            else:
                user.phone = phone
                user.save()
        # 邮箱修改
        email = request.POST.get('email', '')
        if email == user.email:
            pass
        else:
            if User.objects.filter(email=email).count() > 0:
                messages.success(request, '邮箱已被使用')
                return redirect("/user/user/{}/".format(uid))
            else:
                user.email = email
                user.save()
        # 简介修改
        desc = request.POST.get('desc', '')
        if desc == user.desc:
            pass
        else:
            user.desc = desc
            user.save()
        messages.success(request, '成功保存')
        return redirect("/user/user/{}/".format(uid))
    return render(request, "user/level1_user.html", locals())


# 用户修改密码
@user_login_req
@user_auth_req
def repwd(request, uid):
    user = User.objects.get(id=uid)
    if request.method == 'POST':
        password_old = request.POST.get('password_old', '')
        password_new = request.POST.get('password_new', '')
        password_new2 = request.POST.get('password_new2', '')
        if check_password(password_old, user.password):
            if password_new == password_new2:
                user.password = make_password(password_new)
                user.save()
                messages.success(request, '修改成功')
                return redirect("/user/repwd/{}/".format(uid))
            else:
                messages.success(request, '两次密码不一致')
        else:
            messages.success(request, '旧密码不正确')
    return render(request, 'user/level1_repwd.html', locals())


# 用户评论记录
@user_login_req
@user_auth_req
def comment(request, uid):
    user = User.objects.get(id=uid)
    comments = Comment.objects.filter(user=user)
    return render(request, 'user/level1_comment.html', locals())


# 用户删除评论记录
@user_login_req
@user_auth_req
def comment_del(request, cid):
    uid = request.session.get('user_id')
    comment = Comment.objects.get(id=cid)
    comment.delete()
    return redirect("/user/comment/{}/".format(uid))


# 用户收藏记录
@user_login_req
@user_auth_req
def articlecol(request, uid):
    user = User.objects.get(id=uid)
    articlecols = Articlecol.objects.filter(user=user)
    return render(request, 'user/level1_articlecol.html', locals())


# 用户删除收藏记录
@user_login_req
@user_auth_req
def articlecol_del(request, cid):
    uid = request.session.get('user_id')
    articlecol = Articlecol.objects.get(id=cid)
    articlecol.delete()
    return redirect("/user/articlecol/{}/".format(uid))
