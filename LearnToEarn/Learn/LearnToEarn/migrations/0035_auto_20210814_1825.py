# Generated by Django 3.1.6 on 2021-08-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0034_auto_20210814_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_pic',
            field=models.ImageField(default='static/images/slider-01.jpg', max_length=500, upload_to='static/uploads', verbose_name='Course Pic'),
        ),
    ]