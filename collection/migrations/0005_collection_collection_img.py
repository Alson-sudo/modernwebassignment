# Generated by Django 3.2.6 on 2021-09-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20210905_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='collection_img',
            field=models.FileField(null=True, upload_to='static/uploads'),
        ),
    ]
