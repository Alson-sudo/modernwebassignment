# Generated by Django 3.2.6 on 2021-09-04 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20210830_2157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallpaper',
            old_name='wall_name',
            new_name='wallpaper_name',
        ),
        migrations.RenameField(
            model_name='wallpaper',
            old_name='wall_price',
            new_name='wallpaper_price',
        ),
    ]
