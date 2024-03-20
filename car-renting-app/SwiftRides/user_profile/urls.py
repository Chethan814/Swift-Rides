from django.urls import path , include
from user_profile import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('signup/', views.Signup, name='signup'),
    
]
