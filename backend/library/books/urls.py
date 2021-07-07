from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:book_id>/', views.details, name="details"),
    path('<int:book_id>/delete/', views.delete, name="delete"),
    path('<int:book_id>/update/', views.update, name="update"),
    path('create/', views.create, name="create"),
]
