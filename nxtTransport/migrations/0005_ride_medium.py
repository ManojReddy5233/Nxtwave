# Generated by Django 5.0.2 on 2024-02-12 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nxtTransport', '0004_ride'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='medium',
            field=models.CharField(default='train', max_length=10),
        ),
    ]
