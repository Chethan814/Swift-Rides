from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Login', views.Login, name='user login'),
    path('Signup', views.Signup, name='user signup'),
    path('UserInfo/', views.UserInfo, name='user info taking'),
]
