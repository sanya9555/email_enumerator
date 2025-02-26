"""pawned_and_owned URL Configuration

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
from django.urls.conf import path
from hunterApp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('domain', views.domain, name="domain"),
    path('pawned', views.pawned, name="pawned"),
    path('about', views.about, name="about"),   
    path('loginuser', views.loginuser, name="loginuser"),
    path('logoutuser', views.logoutuser, name="logoutuser"),
    path('signuser', views.signuser, name="signuser"),
    path("addForm",views.addForm, name="addForm")
]