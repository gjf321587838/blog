import os

from django.http import HttpResponse


def expression(request):
    m = os.getcwd()
    print(m)
    path = "F:\demo\static\editor\images"
    print(path)
    allfile(path)
    return HttpResponse("ww")


def allfile(basepath):
    for item in os.listdir(basepath):
        path = os.path.join(basepath,item)
        if os.path.isfile(path):
            print(path)
        else:
            allfile(path)
