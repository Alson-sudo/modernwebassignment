# Generated by Django 3.2.6 on 2021-09-29 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0010_auto_20210930_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='wallpaper',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.wallpaper'),
        ),
    ]
