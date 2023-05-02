# Generated by Django 4.2 on 2023-04-28 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_organization_details_branches'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization_details',
            name='branches',
        ),
        migrations.AddField(
            model_name='organization_details',
            name='branches',
            field=models.ManyToManyField(blank=True, related_name='organizations', to='blog.branch'),
        ),
    ]