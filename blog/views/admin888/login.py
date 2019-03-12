from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog import models
import time, datetime


# 管理员登录
def Login(request):
    err = ""
    if request.method == "POST":
        username = request.POST.get("username", None)
        pwd = request.POST.get("pwd", None)
        try:
            u = models.User.objects.get(username=username)
            if u.login_limit < datetime.datetime.now():
                if pwd == u.pwd:
                    request.session["is_login"] = True
                    request.session["u_id"] = u.id
                    request.session["ip"] = request.META["REMOTE_ADDR"]
                    u.last_ip = request.META["REMOTE_ADDR"]
                    u.err_cs = 0
                    u.save()
                    return redirect("/admin/index/")
                else:
                    u.err_cs = u.err_cs + 1
                    err = "您的账号或密码错误！(还有%d次机会)" % (3 - u.err_cs)
                    if u.err_cs == 3:
                        u.err_cs = 0
                        u.login_limit = (datetime.datetime.now() +
                                         datetime.timedelta(minutes=10)).strftime("%Y-%m-%d %H:%M:%S")
                    u.save()
            else:
                m = (u.login_limit - datetime.datetime.now()).seconds
                err = "您的账号被限制登录！(%d分%d秒)" % (m // 60, m % 60)
        except:
            err = "您的用户名或密码错误"
    return render(request, "admin888/login.html", {"err": err})


# 注销登录
def Logout(request):
    request.session.flush()
    return redirect("/admin/login/")


