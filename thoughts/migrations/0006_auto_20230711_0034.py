# Generated by Django 3.2.19 on 2023-07-10 22:34

import colorfield.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0005_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='bg_color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='tag',
            name='text_color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None),
        ),
        migrations.AlterField(
            model_name='thought',
            name='time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
