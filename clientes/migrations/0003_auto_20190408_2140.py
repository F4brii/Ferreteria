# Generated by Django 2.2 on 2019-04-09 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20190408_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
        ),
    ]
