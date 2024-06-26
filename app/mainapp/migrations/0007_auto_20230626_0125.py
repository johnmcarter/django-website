# Generated by Django 3.2.5 on 2023-06-26 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('cover_image', models.ImageField(upload_to='car_images/')),
            ],
        ),
        migrations.CreateModel(
            name='CarPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='car_images/')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.car')),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
