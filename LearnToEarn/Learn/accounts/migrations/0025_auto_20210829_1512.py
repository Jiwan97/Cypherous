# Generated by Django 3.1.6 on 2021-08-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20210819_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default=None, max_length=500, upload_to='static/uploads', verbose_name='ProfilePic'),
        ),
    ]