# Generated by Django 3.0.4 on 2020-03-12 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField()),
                ('libelle', models.TextField()),
                ('annee_debut', models.TextField()),
                ('annee_fin', models.TextField()),
            ],
        ),
    ]
