# Generated by Django 4.2 on 2023-09-16 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_shippingaddress_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_order',
        ),
    ]
