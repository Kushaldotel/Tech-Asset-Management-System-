# Generated by Django 4.2 on 2023-05-12 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0049_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='purchase_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='software',
            name='purchase_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]