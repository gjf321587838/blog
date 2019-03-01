# 登录验证

from django.shortcuts import render,redirect


# 是否登录验证
def is_login(func):
    '''自定义 登录验证 装饰器'''
    def check_login(request):
        '''检查登录状态'''
        if request.session.has_key('is_login'):
            # 当前有用户登录，正常跳转
            return func(request)
        else:
            # 当前没有用户登录，跳转到登录页面
            return redirect('/index/')
    return check_login