# Generated by Django 3.1.6 on 2021-08-13 09:36

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0022_auto_20210813_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodule',
            name='ModuleLecture',
            field=ckeditor.fields.RichTextField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Module Lecture'),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='module',
            field=models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='ModuleName'),
        ),
    ]
