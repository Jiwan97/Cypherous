# Generated by Django 3.1.6 on 2021-08-24 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LearnToEarn', '0064_auto_20210825_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examquestion',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
