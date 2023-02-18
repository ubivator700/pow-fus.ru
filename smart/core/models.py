from django.db import models


class Companies(models.Model):
    company_id = models.IntegerField(auto_created=True, blank=False)
    company_name = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ['company_id']


class Users(models.Model):
    user_id = models.IntegerField(auto_created=True, blank=False)
    user_name = models.CharField(max_length=200, blank=False, default='Пользователь')
    user_role = models.CharField(max_length=100, default='user')
    user_photo = models.ImageField()
    company_name = models.ForeignKey(Companies, on_delete=models.CASCADE)

    class Meta:
        ordering = ['user_id']
