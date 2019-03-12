from django.urls import path
from blog.views.admin888 import login, index, article, system
from blog.views.com import expression

# 后台URL
urlpatterns = [
    path(r'login/', login.Login, name="login"),
    path(r'logout/', login.Logout, name="logout"),
    path(r'index/', index.Index, name="index"),
    path(r'personal/', index.Personal, name="personal"),
    path(r'personal/mod/', index.Personal_mod),
    # 文章类别管理
    path(r'category/', article.Category, name="category"),
    path(r'category/add/', article.Category_add, name="category_add"),
    path(r'category/mod/<int:num>/', article.Category_mod, name="category_mod"),
    path(r'category/del/<int:num>/', article.Category_del, name="category_del"),

    # 文章管理
    path(r'article/', article.Article, name='article'),
    path(r'article/add/', article.Article_add, name='article_add'),
    path(r'article/mod/<int:num>/', article.Article_mod, name='article_mod'),
    path(r'article/del/<int:num>/', article.Article_del, name='article_del'),

    # 系统设置
    path(r'pwd/', system.Pwd, name="pwd"),
    path(r'pwd_mod/', system.Pwd_mod, name="pwd_mod"),
    path(r'expression/', expression.expression, name='expression')
]
