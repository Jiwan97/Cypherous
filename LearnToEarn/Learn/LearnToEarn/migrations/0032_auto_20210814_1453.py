# Generated by Django 3.1.6 on 2021-08-14 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LearnToEarn', '0031_auto_20210814_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseenrollement',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
