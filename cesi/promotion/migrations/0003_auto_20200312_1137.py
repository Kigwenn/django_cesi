# Generated by Django 3.0.4 on 2020-03-12 10:37

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0002_auto_20200312_1025'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='promotion',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]