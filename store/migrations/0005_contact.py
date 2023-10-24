# Generated by Django 4.2 on 2023-07-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_category_product_desc_product_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(default='', max_length=50)),
                ('area', models.CharField(default='', max_length=300)),
                ('phone', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
