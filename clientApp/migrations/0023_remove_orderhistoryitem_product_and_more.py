# Generated by Django 4.2.7 on 2023-12-12 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0022_remove_orderhistory_orders_orderhistory_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderhistoryitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderhistoryitem',
            name='quantity',
        ),
    ]
