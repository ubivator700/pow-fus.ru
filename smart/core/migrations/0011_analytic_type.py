# Generated by Django 4.1.7 on 2023-02-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_expenses_analytic_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytic',
            name='type',
            field=models.TextField(default='line'),
        ),
    ]