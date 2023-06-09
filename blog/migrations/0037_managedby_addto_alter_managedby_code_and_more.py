# Generated by Django 4.2 on 2023-05-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_managedby_code_managedby_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='managedby',
            name='Addto',
            field=models.ManyToManyField(to='blog.branch', verbose_name='Add To Branch'),
        ),
        migrations.AlterField(
            model_name='managedby',
            name='code',
            field=models.CharField(max_length=20, null=True, verbose_name='Branch Code'),
        ),
        migrations.AlterField(
            model_name='managedby',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Branch Name'),
        ),
    ]
