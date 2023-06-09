# Generated by Django 4.2 on 2023-05-01 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_documentcategory_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.vendor'),
        ),
        migrations.AlterField(
            model_name='software',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.vendor'),
        ),
    ]
