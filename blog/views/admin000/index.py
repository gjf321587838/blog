from django.shortcuts import render, redirect
from django.http import HttpResponse


def Index(request):
    return render(request, "admin000/base.html")