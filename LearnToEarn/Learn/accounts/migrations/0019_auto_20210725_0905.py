# Generated by Django 3.1.6 on 2021-07-25 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20210725_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='BirthDate(mm/dd/year)'),
        ),
    ]
