# Generated by Django 4.2.7 on 2023-12-12 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellerApp', '0009_alter_product_discount'),
        ('clientApp', '0020_orderhistory_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderhistory',
            name='cart',
        ),
        migrations.CreateModel(
            name='OrderHistoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientApp.currentorder')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sellerApp.product')),
            ],
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientApp.orderhistoryitem'),
        ),
    ]
