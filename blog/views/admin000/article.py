from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog import models


# 文章分类- 添加
def Classification_add(request):
    if request.method == "POST":
        flm = request.POST.get("flm", None)
        if flm:
            new_category = models.Category()
            new_category.name = flm
            new_category.save()
    return render(request, 'admin000/classification_add.html')


# 文章分类
def Classification(request):
    data = models.Category.objects.all().order_by('id')
    return render(request, 'admin000/classification.html', {"classification": data})


# 文章分类 - 删除
def Classification_del(request, num):
    try:
        models.Category.objects.get(id=num).delete()
    except Exception as e:
        pass
    return redirect("/admin000/classification/")


# 文章分类 - 编辑
def Classification_mod(request, num):
    if request.method == "POST":
        bh = request.POST.get("bh", None)
        flm = request.POST.get("flm", None)
        if bh and flm:
            u = models.Category.objects.get(id=int(bh))
            u.name = flm
            u.save()
        return redirect("/admin000/classification/")
    else:
        try:
            data = models.Category.objects.get(id=num)
            return render(request, 'admin000/classification_add.html', {"yssj":data})
        except Exception as e:
            return redirect("/admin000/classification/")