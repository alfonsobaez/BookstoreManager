# Generated by Django 4.2.4 on 2024-02-23 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='description',
            new_name='descripcion',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='image',
        ),
        migrations.AddField(
            model_name='libro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
    ]
