# Generated by Django 3.1.6 on 2021-07-13 22:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20210714_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sendNotification',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(default='Not Updated', max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
