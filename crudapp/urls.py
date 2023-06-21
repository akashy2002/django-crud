from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('crud', views.crudpage, name="crudpage"),
    path('login', views.handleLogin, name="LoginPage"),
    path('signup', views.handlesignup, name="SignupPage"),
    path('img', views.userimg, name="userImg"),
    path('logout', views.handleLogout, name="logoutpage"),
    path('delete/<str:id>', views.delete, name="delete"),
    path('update/<str:id>', views.update, name="update"),


]
