# Generated by Django 3.2.19 on 2023-06-28 09:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0004_customgroup_customuser_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Untitled Event', max_length=200)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
                ('recurrence', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='customgroup',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
