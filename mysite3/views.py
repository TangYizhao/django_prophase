from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from bookstore.models import Book


def test_base(request):
    list = ["jack","Lily"]
    # print(111111111111111111111111111)
    # print(reverse("pag", args = [300]))
    return render(request,"base.html",locals())

def test_music(request):
    return render(request,"music.html")

def test_pagen(request,num):

    return HttpResponse("test pagen:%s is ok"%num)

def static(request):

    return render(request,"static.html")

def set_cookies(request):
    value = request.COOKIES.get("username", "no value")

    resp = HttpResponse("the cookies key uuname is %s" % value)
    resp.set_cookie("uuname","gulinazha",600)
    # resp.set_cookie("uuname","gulinazha")

    return resp


def get_cookies(request):

     value = request.COOKIES.get("uuname","no value")
     resp=HttpResponse("the cookies key uuname is %s" % value)
     resp.set_cookie("username", "dilireba", 600)
     # value = request.COOKIES["uuname"]
     return resp

def delete_cookies(request):
    resp = HttpResponse("del cookies")
    resp.delete_cookie("uuname")
    return resp

def set_session(request):
    request.session["uname"] = "迪丽热巴"
    return HttpResponse("set session")

def get_session(request):

    value = request.session.get("uname","no value")
    return HttpResponse("session value is %s"%value)
