# Generated by Django 4.2.2 on 2023-06-28 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0008_customgroup_id_alter_customgroup_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customgroup',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
