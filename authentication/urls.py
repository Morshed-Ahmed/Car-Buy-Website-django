from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.UserSignup, name = 'signup'),
    path('login/',views.UserLogin, name = 'login'),
    path('profile/',views.profile, name = 'profile'),
    path('logout/',views.LogOut, name = 'logout'),
]
