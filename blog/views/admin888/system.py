from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.views.admin888.login_check import is_login, is_login_id
from blog import models


@is_login
def Pwd(request):
    return render(request, 'admin888/mod_pwd.html')


# 修改密码
@is_login
def Pwd_mod(request):
    if request.method == "POST":
        old_pwd = request.POST.get("old_pwd", None)
        new_pwd = request.POST.get("new_pwd", None)
        qr_pwd = request.POST.get("qr_pwd", None)
        if old_pwd and new_pwd and qr_pwd:
            if new_pwd == qr_pwd:
                try:
                    user = models.User.objects.get(username="admin")
                    print(user.pwd)
                    if old_pwd == user.pwd:
                        user.pwd = old_pwd
                        user.save()
                    else:
                        message = "原密码不正确!"
                except:
                    message = "出现异常!"
            else:
                message = "两次密码不一致!"
        else:
            message = "输入的数据不完善!"
    return render(request, 'admin888/mod_pwd.html', locals())