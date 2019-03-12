# 登录验证
from django.shortcuts import render,redirect


# 是否登录验证
def is_login(func):
    def check_login(request):
        if request.session.has_key('is_login'):
            return func(request)
        else:
            return redirect('/admin/login/')
    return check_login


# 有参数的登录验证
def is_login_id(func):
    def check_login(*args, **kwargs):
        # if args[0].META.has_key('HTTP_X_FORWARDED_FOR'):
        #     ip = args[0].META['HTTP_X_FORWARDED_FOR']
        # else:
        ip = args[0].META['REMOTE_ADDR']
        if args[0].session.has_key('is_login'):
            return func(args[0], kwargs.get("num", None))
        else:
            return redirect('/admin/login/')
    return check_login
