from seats.views import SeatsViewSet
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
        
router = routers.SimpleRouter(trailing_slash=False)
router.register(r'seats', SeatsViewSet, basename='seats')


urlpatterns = [
    # path('books/', include('books.urls')),
    # path('admin/', admin.site.urls)
]
urlpatterns += router.urls
