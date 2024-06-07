# Generated by Django 5.0.6 on 2024-05-31 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plant',
            options={'ordering': ('-content',)},
        ),
        migrations.AddField(
            model_name='plant',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='plant',
            index=models.Index(fields=['-time_created'], name='plants_plan_time_cr_2fa7f5_idx'),
        ),
    ]