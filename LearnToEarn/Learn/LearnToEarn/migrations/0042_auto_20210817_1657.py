# Generated by Django 3.1.6 on 2021-08-17 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0041_auto_20210817_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursereview',
            name='date_commented',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursereview',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, '1-Star'), (2, '2-Star'), (3, '3-Star'), (4, '4-Star'), (5, '5-Star')], default=12),
            preserve_default=False,
        ),
    ]
