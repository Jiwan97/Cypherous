# Generated by Django 3.1.6 on 2021-08-13 09:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0020_auto_20210812_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodule',
            name='ModuleLecture',
            field=models.CharField(default='Not Updated', max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Module Lecture'),
        ),
    ]
