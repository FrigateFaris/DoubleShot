# Generated by Django 4.2.7 on 2023-12-11 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0016_remove_orderhistory_client_orderhistory_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientApp.client'),
        ),
    ]
