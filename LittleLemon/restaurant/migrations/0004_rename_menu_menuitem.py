# Generated by Django 4.2.6 on 2023-10-14 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_menu'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='MenuItem',
        ),
    ]