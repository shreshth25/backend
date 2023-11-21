from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.UserRegistration.as_view() ,name='register'),
    path('login/', views.UserLogin.as_view() ,name='login'),
    path('profile/', views.UserProfile.as_view() ,name='profile'),
    path('post/', views.PostView.as_view() ,name='post'),
    path('reel/', views.ReelView.as_view() ,name='reel'),

    
]
