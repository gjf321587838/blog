from django.urls import path
from blog.views.admin000 import index,personal, article
from blog.views.com import expression

# 后台URL
urlpatterns = [
    path(r'index/', index.Index),
    # 个人资料
    path(r'personal/', personal.Personal, name="personal"),
    path(r'personal/add/', personal.Personal_add, name="personal_add"),

    # 文章管理
    path(r'classification/', article.Classification, name="classification"),
    path(r'classification/add/', article.Classification_add, name="classification_add"),
    path(r'classification/del/<int:num>/', article.Classification_del, name="classification_del"),
    path(r'classification/mod/<int:num>/', article.Classification_mod, name="classification_mod"),




]


