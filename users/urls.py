from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('authenticate/', views.authenticateUser, name='authenticate'),
    path('register/', views.registerUser, name='register'),
    path('createUser/', views.createUser, name='createUser'),
    path('logout', views.logoutUser, name='logout')
]