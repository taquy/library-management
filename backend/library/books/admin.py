from django.contrib import admin
from .models import Book
# Register your models here.

admin.site.site_header = "Library Management Admin"
admin.site.site_title = "Library Management Admin Area"
admin.site.register(Book)
