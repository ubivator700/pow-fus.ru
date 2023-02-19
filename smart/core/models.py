from django.db import models


USER_ROLE_CHOICE = [
    ('director', 'Директор'),
    ('top-manager', 'Топ-менеджер'),
    ('manager','Менеджер')
]


class Companies(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ['company_id']

    def __str__(self):
        return self.company_name


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, default='Пользователь')
    company_name = models.CharField(max_length=200, default='company')
    avatar = models.TextField()
    role = models.TextField(choices=USER_ROLE_CHOICE, default='manager')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
    

class Analytic(models.Model):
    name = models.CharField(max_length=200, default='chart')
    price = models.IntegerField(default=0, blank=False)
    series = models.JSONField()

    def __str__(self):
        return self.name
