# Generated by Django 3.2.6 on 2021-09-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_profiles_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='profile_pic',
            field=models.FileField(default='static/img/clown.jpg', upload_to='static/profile'),
        ),
    ]