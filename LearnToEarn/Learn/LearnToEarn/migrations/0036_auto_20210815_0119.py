# Generated by Django 3.1.6 on 2021-08-14 19:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0035_auto_20210814_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_summary',
            field=models.CharField(default='Not Updated', max_length=200, null=True, verbose_name='Course Summary'),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='ModuleLecture',
            field=ckeditor.fields.RichTextField(max_length=50000, null=True, verbose_name='Module Lecture'),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='module',
            field=models.CharField(max_length=200, null=True, verbose_name='Module Name'),
        ),
        migrations.AlterField(
            model_name='coursereview',
            name='comment',
            field=models.CharField(default='Not Updated', max_length=200, null=True),
        ),
    ]
