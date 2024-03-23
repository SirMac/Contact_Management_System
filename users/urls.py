from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.loginIndex, name='login'),
    path('authenticate/', views.authenticateUser, name='authenticate'),
    path('register/', views.register, name='register'),
    path('logout', views.logoutUser, name='logout')
]