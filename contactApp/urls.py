
from django.contrib import admin
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('accounts/', include('users.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
    re_path(r'static/(.+)', views._static_butler)
]
