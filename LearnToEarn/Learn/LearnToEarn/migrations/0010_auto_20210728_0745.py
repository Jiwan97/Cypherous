# Generated by Django 3.1.6 on 2021-07-28 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0009_auto_20210727_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_pic',
            field=models.ImageField(default='static/images/newsDefault.jpg', max_length=500, upload_to='static/uploads', verbose_name='News Pic'),
        ),
    ]
