# Generated by Django 3.1.6 on 2021-07-28 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0011_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='responded',
            field=models.BooleanField(default=False),
        ),
    ]
