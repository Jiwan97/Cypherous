# Generated by Django 3.1.6 on 2021-08-13 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0025_auto_20210813_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_summary',
            field=models.CharField(default='Not Updated', max_length=200, null=True, verbose_name='Course Name'),
        ),
    ]
