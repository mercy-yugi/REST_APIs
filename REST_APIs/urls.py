from unicodedata import name
from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView
urlpatterns = [
  path('get-details/',UserDetailAPI.as_view(),name='login'),
  path('register/',RegisterUserAPIView.as_view(), name='register'),
  
]