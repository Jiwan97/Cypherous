# Generated by Django 3.1.6 on 2021-07-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0012_contactmessage_responded'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='Tags',
            field=models.CharField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five')], default='Not Updated', max_length=200, null=True, verbose_name='Tags'),
        ),
    ]
