# Generated by Django 4.2 on 2023-05-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0055_assetrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetrequest',
            name='priority',
            field=models.CharField(choices=[('Uregent', 'Uregent'), ('High', 'High'), ('Medium', 'Medium'), ('low', 'low')], max_length=10),
        ),
        migrations.AlterField(
            model_name='assetrequest',
            name='status',
            field=models.CharField(choices=[('Request', 'Request'), ('Approve', 'Approve'), ('Cancel', 'Cancel')], max_length=255),
        ),
    ]
