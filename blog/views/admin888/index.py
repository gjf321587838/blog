from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.views.admin888.login_check import is_login, is_login_id
from blog import models


# 后台首页
@is_login
def Index(request):
    return render(request, "admin888/index.html")


# 个人介绍
@is_login
def Personal(request):
    u_info = models.User.objects.get(id=request.session.get("u_id"))
    nickname = u_info.nickname
    gender = u_info.gender
    introduce = u_info.introduce
    return render(request, "admin888/personal.html", locals())


# 编辑介绍
@is_login
def Personal_mod(request):
    if request.method == "POST":
        nickname = request.POST.get("nickname", None)
        gender = request.POST.get("gender", None)
        introduce = request.POST.get("introduce", None)
        try:
            u = models.User.objects.get(id=int(request.session.get("u_id")))
            u.nickname = nickname
            u.gender = gender
            u.introduce = introduce
            u.save()
        except:
            pass
    return redirect("/admin/personal/")


