# Generated by Django 4.1.7 on 2023-03-21 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Siteweb', '0002_rename_userinfo_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserInfo',
        ),
    ]