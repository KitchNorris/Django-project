# Generated by Django 4.1.4 on 2023-02-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
