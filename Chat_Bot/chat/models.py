from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    # Specify unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='chat_users',  # Use a unique related_name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='chat_users',  # Use a unique related_name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    class Meta:
        # Specify any meta options here, such as permissions
        permissions = [
            ("can_publish", "Can publish posts"),
            ("can_edit", "Can edit posts"),
            ("can_delete", "Can delete posts"),
        ]
        default_permissions = ()

    def __str__(self):
        return self.username
class ChatHistory(models.Model):
    # Define your ChatHistory model fields here
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message: {self.message[:20]}"

    class Meta:
        verbose_name_plural = "Chat History"