# Generated by Django 5.0.3 on 2024-05-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly')], default='W', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]