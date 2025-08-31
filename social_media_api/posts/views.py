from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


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

class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"detail": "Already liked."}, status=status.HTTP_200_OK)

        # create notification to post author (skip self-like notify)
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id,
            )
        return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)


class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        deleted, _ = Like.objects.filter(user=request.user, post=post).delete()
        if deleted:
            return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
        return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
    