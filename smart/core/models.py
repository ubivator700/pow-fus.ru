from django.db import models


class Owners(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner_name = models.CharField(max_length=200, blank=True, default='')
    role = models.CharField(max_length=100, default='user')

    class Meta:
        ordering = ['created']
