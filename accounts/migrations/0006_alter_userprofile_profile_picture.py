# Generated by Django 4.0.2 on 2022-04-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='user_profile'),
        ),
    ]