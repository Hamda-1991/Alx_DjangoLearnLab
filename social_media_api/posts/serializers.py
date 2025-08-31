from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import UserSerializer
from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']

# posts/serializers.py (add fields inside your PostSerializer)

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments', 'likes_count']
        read_only_fields = ['author', 'created_at', 'updated_at', 'comments', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()
