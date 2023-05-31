# Generated by Django 4.2 on 2023-04-29 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypost', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
