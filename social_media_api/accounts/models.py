# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # directional follow relationship:
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username

    # convenience helpers (optional)
    def follow(self, other_user):
        if other_user != self:
            self.following.add(other_user)

    def unfollow(self, other_user):
        if other_user != self:
            self.following.remove(other_user)

    @property
    def followers_count(self):
        return self.followers.count()

    @property
    def following_count(self):
        return self.following.count()

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers', blank=True
    )

    def __str__(self):
        return self.username