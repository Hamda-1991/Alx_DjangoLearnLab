# bookshelf/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Replace with your actual view
    path('form/', views.form_example_view, name='form'),
    path('search/', views.search_books, name='search'),
]
