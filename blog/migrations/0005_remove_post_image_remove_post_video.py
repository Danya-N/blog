# Generated by Django 5.1.5 on 2025-04-09 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image_post_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='video',
        ),
    ]
