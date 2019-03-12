from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog import models

# 首页


def Index(request):
    m = {}
    m["u_info"] = models.User.objects.get(username="admin")
    m["article"] = models.Article.objects.filter()
    m["category"] = models.Category.objects.filter()
    return render(request, 'front/index.html', m)