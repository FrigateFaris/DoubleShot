# Generated by Django 4.2.7 on 2023-12-04 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellerApp', '0008_discountcoupon'),
        ('clientApp', '0008_cart_general_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=255)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_address', models.CharField(max_length=255)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('status', models.BooleanField()),
                ('cart', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientApp.cart')),
                ('discount_coupon', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sellerApp.discountcoupon')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientApp.client')),
            ],
        ),
    ]