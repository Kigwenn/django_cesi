# Generated by Django 3.0.4 on 2020-03-12 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0003_auto_20200312_1137'),
        ('membre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membre',
            name='promotion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='promotion.Promotion'),
        ),
    ]
