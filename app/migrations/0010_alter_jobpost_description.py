# Generated by Django 5.0.3 on 2024-05-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_jobpost_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.TextField(),
        ),
    ]
