from django.shortcuts import render, redirect
from django.http import HttpResponse


# 个人资料
def Personal(request):
    return render(request, "admin000/personal.html")


# 编辑个人资料
def Personal_add(request):
    if request.method == "POST":
        u_name = request.POST.get("u_name", None)
        u_email = request.POST.get("u_email", None)
        u_phone = request.POST.get("u_phone", None)
        u_qq = request.POST.get("u_qq", None)
        u_wb = request.POST.get("u_wb", None)
        u_grjs = request.POST.get("u_grjs", None)
        print(u_name, u_phone, u_email, u_qq, u_wb, u_grjs)
        pass
    return redirect("/admin000/personal")

