from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView, UserFollowersView, UserFollowingView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
     # follow/unfollow routes
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow'),

    # optional listing
    path('<int:user_id>/followers/', UserFollowersView.as_view(), name='user-followers'),
    path('<int:user_id>/following/', UserFollowingView.as_view(), name='user-following'),
]
