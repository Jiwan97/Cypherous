# Generated by Django 3.1.6 on 2021-07-11 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210712_0347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone',
            new_name='phonenumber',
        ),
    ]
