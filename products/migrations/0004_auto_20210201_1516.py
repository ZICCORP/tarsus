# Generated by Django 3.1.5 on 2021-02-01 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
