from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    is_admin = models.BooleanField('is_admin', default=False)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='myapp_user_set',  # Add related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='myapp_user_set',  # Add related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

    def __str__(self):
        return self.username
