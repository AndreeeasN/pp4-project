# Generated by Django 3.2.19 on 2023-06-23 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0004_auto_20230623_0223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_created']},
        ),
    ]
