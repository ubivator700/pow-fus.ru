# Generated by Django 4.1.7 on 2023-02-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_action_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='series',
            field=models.TextField(),
        ),
    ]
