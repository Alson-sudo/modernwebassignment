# Generated by Django 3.2.6 on 2021-09-23 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='content_audio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='content_image',
        ),
    ]
