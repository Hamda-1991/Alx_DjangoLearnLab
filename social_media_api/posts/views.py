from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# Standard pagination for posts & comments
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        # Automatically assign logged-in user as author
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        # Automatically assign logged-in user as author
        serializer.save(author=self.request.user)


# Custom pagination for feed
class FeedPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # get all the users the current user is following
        following_users = request.user.following.all()

        # fetch posts by followed users, ordered by creation date DESC
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        # serialize the posts
        data = [
            {
                "id": post.id,
                "author": post.author.username,
                "content": post.content,
                "created_at": post.created_at
            }
            for post in posts
        ]
        return Response(data)