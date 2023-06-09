# Generated by Django 4.2 on 2023-04-27 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_document_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.status'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='service_tag',
            field=models.CharField(editable=False, max_length=8, unique=True),
        ),
    ]
