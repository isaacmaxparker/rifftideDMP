from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    STATUS_CHOICES = (
            ('A', 'Active'),
            ('I', 'Inactive')
    )

    name = models.TextField(default='NONE')
    loginname = models.TextField(default='NONE')
    voicepart = models.TextField(default='NONE')
    status = models.TextField(db_index=True, choices=STATUS_CHOICES, default='A')
