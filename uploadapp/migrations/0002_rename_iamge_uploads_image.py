# Generated by Django 5.0.3 on 2024-05-08 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploads',
            old_name='iamge',
            new_name='image',
        ),
    ]
