# Generated by Django 4.2.7 on 2023-12-11 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0012_alter_orderhistory_delivered_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderhistory',
            name='client',
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='client',
            field=models.ManyToManyField(blank=True, to='clientApp.client'),
        ),
    ]