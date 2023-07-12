# Generated by Django 4.2.2 on 2023-07-12 11:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0045_alter_customgroup_members_alter_customgroup_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customgroup',
            name='members',
            field=models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)], verbose_name='Nombre de membres'),
        ),
    ]
