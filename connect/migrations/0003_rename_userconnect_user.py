# Generated by Django 4.1.6 on 2023-02-08 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('connect', '0002_rename_user_userconnect'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserConnect',
            new_name='User',
        ),
    ]
