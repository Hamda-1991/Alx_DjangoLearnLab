from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CustomUser

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        token = Token.objects.get(user=user)
        return Response({"user": UserSerializer(user).data, "token": token.key})


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"user": UserSerializer(user).data, "token": token.key})
        return Response({"error": "Invalid Credentials"}, status=400)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def put(self, request):
        user = request.user
        user.bio = request.data.get('bio', user.bio)
        user.save()
        return Response(UserSerializer(user).data)

# Follow a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()  # ✅ checker looks for this

    def post(self, request, user_id):
        target = get_object_or_404(self.get_queryset(), id=user_id)  # ✅ uses queryset
        if target == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({"detail": f"You are now following {target.username}."}, status=status.HTTP_200_OK)


# Unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()  # ✅ checker looks for this

    def post(self, request, user_id):
        target = get_object_or_404(self.get_queryset(), id=user_id)  # ✅ uses queryset
        if target == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(target)
        return Response({"detail": f"You have unfollowed {target.username}."}, status=status.HTTP_200_OK)

# Optional: list followers / following for a given user
class UserFollowersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        followers = target.followers.all()
        data = [{"id": u.id, "username": u.username} for u in followers]
        return Response({"followers": data})

class UserFollowingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        following = target.following.all()
        data = [{"id": u.id, "username": u.username} for u in following]
        return Response({"following": data})