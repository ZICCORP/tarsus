# Generated by Django 3.1.5 on 2021-02-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210201_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]
