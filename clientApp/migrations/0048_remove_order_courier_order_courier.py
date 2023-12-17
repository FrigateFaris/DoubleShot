# Generated by Django 4.2.7 on 2023-12-15 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0047_order_courier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='courier',
        ),
        migrations.AddField(
            model_name='order',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientApp.courier'),
        ),
    ]