# Generated by Django 2.0.2 on 2018-04-26 02:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20180426_0216'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='Profile',
        ),
    ]
