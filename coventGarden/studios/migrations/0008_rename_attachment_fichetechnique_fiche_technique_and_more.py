# Generated by Django 4.2.2 on 2023-06-28 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0007_fichetechnique_remove_customuser_fichetechnique'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fichetechnique',
            old_name='attachment',
            new_name='Fiche_Technique',
        ),
        migrations.AddField(
            model_name='fichetechnique',
            name='Utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
