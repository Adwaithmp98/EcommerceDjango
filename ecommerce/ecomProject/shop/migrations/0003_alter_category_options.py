# Generated by Django 4.1.7 on 2023-03-08 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_catogory_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'catogory', 'verbose_name_plural': 'catogories'},
        ),
    ]
