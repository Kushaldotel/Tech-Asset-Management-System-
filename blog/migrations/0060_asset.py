# Generated by Django 4.2 on 2023-05-18 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0059_remove_document_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware', models.BooleanField(default=True)),
            ],
        ),
    ]
