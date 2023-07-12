# Generated by Django 4.2.2 on 2023-07-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0029_alter_technicalsheet_pdf_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicalsheet',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='media/public'),
        ),
        migrations.AlterField(
            model_name='technicalsheet',
            name='pdf_logo',
            field=models.FileField(blank=True, null=True, upload_to='media/public'),
        ),
    ]
