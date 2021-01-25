"""mysite3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''
user:   Tyz_admin
email:  3140105268@zju.edu.cn
Password:   tyz_123456
'''


from django.contrib import admin
from django.urls import path, include

from mysite3 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("test_base",views.test_base),

    path("test_music",views.test_music,name="mus"),

    path("page/<int:num>",views.test_pagen,name = "pag"),

    path("static",views.static),

    path("music/",include("music.urls")),

    path("news/",include("news.urls")),

    path("sports/",include("sports.urls")),

    path("bookstore/",include("bookstore.urls")),

    path("set_cookies",views.set_cookies),

    path("get_cookies",views.get_cookies),

    path("delete_cookies",views.delete_cookies),

    path("set_session",views.set_session),

    path("get_session",views.get_session),

]
