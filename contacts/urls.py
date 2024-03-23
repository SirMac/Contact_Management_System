from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.createContact, name='createContact'),
    path('read', views.readContact, name='readContact'),
    path('update', views.updateContact, name='updateContact'),
    path('delete', views.deleteContact, name='deleteContact'),
]