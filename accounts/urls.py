from django.urls import path ,include
from accounts.views import Registration , Profile
from django.contrib import auth




urlpatterns = [
    
    path('',include('django.contrib.auth.urls')),
    path('register',Registration.as_view(),name='register'),
    path('profile/',Profile.as_view(),name='profile'),
    
]


 