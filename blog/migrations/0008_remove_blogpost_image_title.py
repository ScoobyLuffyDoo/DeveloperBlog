# Generated by Django 4.0.2 on 2022-02-27 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpost_image_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='image_title',
        ),
    ]
