# Generated by Django 4.2 on 2023-04-30 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypost', '0013_alter_comment_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comm',
            new_name='post',
        ),
    ]