# Generated by Django 3.1.6 on 2021-08-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0061_auto_20210824_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examqna',
            name='answer',
            field=models.CharField(max_length=5000, null=True, verbose_name='Answer'),
        ),
    ]
