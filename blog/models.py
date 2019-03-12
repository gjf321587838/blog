from django.db import models

# Create your models here.


# 用户表
class User(models.Model):
    username = models.CharField(max_length=32, verbose_name="用户名")
    pwd = models.CharField(max_length=255, verbose_name="密码")
    login_limit = models.DateTimeField(auto_now_add=True, verbose_name="限制登录时间")
    err_cs = models.IntegerField(verbose_name="错误次数")
    nickname = models.CharField(max_length=32, default="未命名", verbose_name="昵称", null=True)
    gender = models.CharField(max_length=2, default="", verbose_name="性别", null=True)
    introduce = models.CharField(max_length=255, verbose_name="自我介绍", null=True)
    last_ip = models.GenericIPAddressField(null=True, protocol="ipv4")


# 文章类别
class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name="文章类别", unique=True)


# 文章
class Article(models.Model):
    title = models.CharField(max_length=32, verbose_name="文章标题")
    category = models.ForeignKey(to=Category, to_field="id", on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField(verbose_name="文章正文")
    art_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)

