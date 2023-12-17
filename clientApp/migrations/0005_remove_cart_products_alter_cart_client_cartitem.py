# Generated by Django 4.2.7 on 2023-11-30 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellerApp', '0007_delete_seller'),
        ('clientApp', '0004_rename_product_id_cart_products_remove_client_cart_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AlterField(
            model_name='cart',
            name='client',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientApp.client'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientApp.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellerApp.product')),
            ],
        ),
    ]
