# Generated by Django 3.1.6 on 2021-08-14 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0030_auto_20210814_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseenrollement',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LearnToEarn.course'),
        ),
    ]
