# Generated by Django 3.1.6 on 2021-08-13 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0026_auto_20210813_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_summary',
            field=models.CharField(default='Not Updated', max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='modulenumber',
            field=models.IntegerField(max_length=200, null=True, verbose_name='Lecture Number'),
        ),
    ]