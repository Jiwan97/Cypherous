# Generated by Django 3.1.6 on 2021-07-12 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210712_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(default='Update Your Name', max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]