# Generated by Django 2.1.2 on 2018-11-08 16:10

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20181108_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='file',
            field=models.FileField(default='', upload_to=mainapp.models.file_directory_path, verbose_name='files'),
        ),
    ]
