# Generated by Django 3.0.4 on 2020-03-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotion',
            name='annee_debut',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='annee_fin',
            field=models.DateTimeField(),
        ),
    ]
