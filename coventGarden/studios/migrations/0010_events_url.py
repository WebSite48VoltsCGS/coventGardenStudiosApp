# Generated by Django 3.2.19 on 2023-06-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0009_events_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
