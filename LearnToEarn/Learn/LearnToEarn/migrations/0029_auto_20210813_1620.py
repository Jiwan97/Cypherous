# Generated by Django 3.1.6 on 2021-08-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0028_auto_20210813_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursemodule',
            options={'ordering': ('modulenumber',)},
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='modulenumber',
            field=models.IntegerField(max_length=30, null=True, verbose_name='Lecture Number'),
        ),
    ]
