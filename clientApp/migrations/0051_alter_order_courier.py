# Generated by Django 4.2.7 on 2023-12-15 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientApp', '0050_alter_order_courier_delete_courier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_as_courier', to=settings.AUTH_USER_MODEL),
        ),
    ]
