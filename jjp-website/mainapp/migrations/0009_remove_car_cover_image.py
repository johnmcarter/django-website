# Generated by Django 3.2.5 on 2023-06-26 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_rename_case_carphoto_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='cover_image',
        ),
    ]
