from django.http import HttpResponse
import os
import json


def expression(request):
    all_path = os.listdir(os.getcwd()+"/static/editor/images")
    emotions = []
    for i in all_path:
        m = os.listdir(os.getcwd()+"/static/editor/images/"+i)
        u = {}
        u["title"] = i
        u["type"] = 'image'
        u["content"] = []
        for j in m:
            e = {}
            e["alt"] = ""
            e["src"] = "/static/editor/images/"+i+"/"+j
            u["content"].append(e)
        emotions.append(u)
    return HttpResponse(emotions)
