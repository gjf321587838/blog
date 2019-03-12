from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.views.admin888.login_check import is_login, is_login_id
from blog import models


# 文章类别
@is_login
def Category(request):
    data = models.Category.objects.filter()
    return render(request, "admin888/category_list.html", {"data": data})


# 文章类别添加
@is_login
def Category_add(request):
    if request.method == "POST":
        wzlb = request.POST.get("wzlb", None)
        if wzlb:
            try:
                new_category = models.Category()
                new_category.name = wzlb
                new_category.save()
                return redirect("/admin/category/")
            except:
                pass
    return render(request, "admin888/category_add.html")


# 修改文章类别名称
@is_login_id
def Category_mod(request, num):
    try:
        old_category = models.Category.objects.get(id=num)
        if request.method == "POST":
            wzlb = request.POST.get("wzlb", None)
            if wzlb:
                old_category.name = wzlb
                old_category.save()
                return redirect("/admin/category/")
        return render(request, 'admin888/category_add.html', {"old_category": old_category})
    except:
        return redirect("/admin/category/")


# 删除文章类别
@is_login_id
def Category_del(request, num):
    try:
        m = models.Category.objects.get(id=num)
        m.delete()
    except:
        pass
    return redirect("/admin/category/")


# 文章列表
@is_login
def Article(request):
    all_article = models.Article.objects.filter()
    return render(request, 'admin888/article.html', {"all_article": all_article})


# 文章添加
@is_login
def Article_add(request):
    m={}
    m["all_category"] = models.Category.objects.filter()
    if request.method == "POST":
        title = request.POST.get("title", None)
        flm = request.POST.get("flm", None)
        content = request.POST.get("content", None)
        if title and flm and content:
            try:
                new_article = models.Article()
                new_article.title = title
                new_article.content = content
                new_article.category = models.Category.objects.get(id=int(flm))
                new_article.save()
                return redirect("/admin/article/")
            except Exception as e:
                pass
    return render(request, 'admin888/article_add.html', m)


# 文章修改
@is_login_id
def Article_mod(request, num):
    data = models.Article.objects.get(id=num)
    all_category = models.Category.objects.filter()
    if request.method == "POST":
        title = request.POST.get("title", None)
        flm = request.POST.get("flm", None)
        content = request.POST.get("content", None)
        if title and flm and content:
            try:
                data.title = title
                data.content = content
                data.category = models.Category.objects.get(id=int(flm))
                data.save()
                return redirect("/admin/article/")
            except Exception as e:
                pass
    return render(request, 'admin888/article_add.html', {"info": data, "all_category": all_category})


# 文章删除
@is_login_id
def Article_del(request, num):
    try:
        models.Article.objects.get(id=num).delete()
    except Exception as e:
        pass
    return redirect("/admin/article/")