# Generated by Django 3.2.5 on 2024-06-25 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_blogpost_value'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='value',
            new_name='rating',
        ),
    ]
