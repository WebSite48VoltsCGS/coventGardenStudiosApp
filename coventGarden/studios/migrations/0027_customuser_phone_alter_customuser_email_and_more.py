# Generated by Django 4.2.2 on 2023-07-06 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0026_remove_customuser_phone_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=10, verbose_name='Numéro de téléphone'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=320, unique=True, verbose_name='Adresse e-mail'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Mot de passe'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name="Nom d'utilisateur"),
        ),
    ]
