# Generated by Django 4.2 on 2023-05-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0051_service_category_service_service_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
