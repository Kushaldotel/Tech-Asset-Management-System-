# Generated by Django 4.2 on 2023-05-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0060_asset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='hardware',
        ),
        migrations.AddField(
            model_name='asset',
            name='hardware_name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]