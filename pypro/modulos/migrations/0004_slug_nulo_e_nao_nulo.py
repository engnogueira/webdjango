# Generated by Django 3.0.2 on 2020-01-13 08:56

from django.db import migrations, models


# import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('modulos', '0003_populando_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(unique=True),
        )
    ]
