# Generated by Django 4.2.6 on 2023-10-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_alter_film_released'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='released',
            field=models.DateField(),
        ),
    ]