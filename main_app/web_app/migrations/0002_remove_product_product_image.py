# Generated by Django 5.0.4 on 2024-04-17 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
    ]