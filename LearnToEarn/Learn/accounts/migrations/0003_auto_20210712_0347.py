# Generated by Django 3.1.6 on 2021-07-11 22:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
