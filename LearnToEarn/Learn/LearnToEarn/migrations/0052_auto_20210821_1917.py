# Generated by Django 3.1.6 on 2021-08-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0051_remove_exammodel_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammodel',
            name='ExamTitle',
            field=models.CharField(default='Not Updated', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='exammodel',
            name='ExamNumber',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Exam Number'),
        ),
    ]
