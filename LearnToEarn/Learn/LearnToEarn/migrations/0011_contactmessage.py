# Generated by Django 3.1.6 on 2021-07-28 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnToEarn', '0010_auto_20210728_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phonenumber', models.CharField(max_length=100, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('query', models.CharField(max_length=1000, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
