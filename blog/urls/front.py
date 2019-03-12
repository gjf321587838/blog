from django.urls import path
from blog.views.front import index

# 前台URL
urlpatterns = [
    path(r'', index.Index),
    path(r'index/', index.Index)

]
