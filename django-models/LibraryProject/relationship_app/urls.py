from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    # ✅ Use Django built-in LoginView and LogoutView with required template names
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

]




urlpatterns = [
    
    path('books/', list_books, name='book-list'),  # function-based view
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),  # class-based view
]
