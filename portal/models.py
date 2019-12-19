from django.db import models

# Create your models here.
class Score(models.Model):

    STATUS_CHOICES = (
            ('A', 'Active'),
            ('I', 'Inactive')
    )

    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField(default='')
    allURL = models.TextField(default='NONE')
    partURL = models.TextField(default='NONE')
    part = models.TextField(default='ALL')
    views = models.IntegerField(default=0)
    status = models.TextField(db_index=True, choices=STATUS_CHOICES, default='A')