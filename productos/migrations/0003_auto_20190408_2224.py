# Generated by Django 2.2 on 2019-04-09 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20190408_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='Productos', verbose_name='Imagen_Producto'),
        ),
    ]