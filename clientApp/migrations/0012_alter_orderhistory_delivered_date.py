# Generated by Django 4.2.7 on 2023-12-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientApp', '0011_orderhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhistory',
            name='delivered_date',
            field=models.DateTimeField(null=True),
        ),
    ]