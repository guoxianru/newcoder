# 定义一个装饰器 去判断用户是否登录，登录成功，就做操作，没有登录就跳转去登录
from django.shortcuts import redirect
from django.http import HttpResponse

def check(func):
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
                return redirect('/blog/login/')
    return inner
