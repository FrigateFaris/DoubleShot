# Generated by Django 4.2.7 on 2023-12-13 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0029_alter_orderitem_order_alter_orderitem_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
    ]
