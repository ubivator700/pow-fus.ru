# Generated by Django 4.1.7 on 2023-02-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_users_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analytic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.IntegerField(default=0)),
                ('expenses', models.IntegerField(default=0)),
                ('revenue', models.IntegerField(default=0)),
                ('data', models.JSONField()),
            ],
        ),
    ]