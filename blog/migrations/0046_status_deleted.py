# Generated by Django 4.2 on 2023-05-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_remove_status_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]