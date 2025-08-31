from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import Comment, Post
from notifications.models import Notification

@receiver(post_save, sender=Comment)
def notify_post_author_on_comment(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        commenter = instance.author
        if post.author != commenter:
            Notification.objects.create(
                recipient=post.author,
                actor=commenter,
                verb="commented on your post",
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id,
            )
