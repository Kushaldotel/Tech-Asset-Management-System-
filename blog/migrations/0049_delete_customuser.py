# Generated by Django 4.2 on 2023-05-11 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0048_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
