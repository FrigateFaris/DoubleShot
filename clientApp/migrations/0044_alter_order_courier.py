# Generated by Django 4.2.7 on 2023-12-15 05:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientApp', '0043_courier_alter_order_courier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='courier',
            field=models.ManyToManyField(null=True, related_name='order_as_courier', to=settings.AUTH_USER_MODEL),
        ),
    ]