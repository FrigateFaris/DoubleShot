# Generated by Django 4.2.7 on 2023-11-30 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellerApp', '0006_product_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Seller',
        ),
    ]