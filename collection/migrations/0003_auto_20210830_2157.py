# Generated by Django 3.2.6 on 2021-08-30 16:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20210830_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='collection_desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='collection_name',
            field=models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
