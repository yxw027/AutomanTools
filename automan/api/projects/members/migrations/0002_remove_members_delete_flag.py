# Generated by Django 2.2.2 on 2020-01-22 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='delete_flag',
        ),
    ]
