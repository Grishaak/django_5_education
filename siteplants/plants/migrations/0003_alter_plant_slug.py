# Generated by Django 5.0.6 on 2024-05-31 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_alter_plant_options_plant_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]