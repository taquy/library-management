from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User

urlpatterns = [
    path('books/', include('books.urls')),
    path('admin/', admin.site.urls)
]
