# Generated by Django 3.1.6 on 2021-08-21 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0052_auto_20210821_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exammodel',
            old_name='date_commented',
            new_name='date',
        ),
    ]
