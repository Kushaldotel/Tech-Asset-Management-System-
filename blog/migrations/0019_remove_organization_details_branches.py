# Generated by Django 4.2 on 2023-04-28 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_organization_details_branches_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization_details',
            name='branches',
        ),
    ]
