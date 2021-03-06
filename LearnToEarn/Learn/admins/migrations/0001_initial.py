# Generated by Django 3.1.6 on 2021-07-28 03:24

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LearnToEarn', '0011_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(default='Not Updated', null=True, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='Your Response Here')),
                ('responded', models.BooleanField(default=False)),
                ('contactMessage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LearnToEarn.contactmessage')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
