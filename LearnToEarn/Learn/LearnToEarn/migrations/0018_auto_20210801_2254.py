# Generated by Django 3.1.6 on 2021-08-01 17:09

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('LearnToEarn', '0017_auto_20210730_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='Tags',
        ),
        migrations.AddField(
            model_name='news',
            name='Tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
