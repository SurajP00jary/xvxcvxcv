# Generated by Django 4.0.1 on 2022-03-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_rename_order_products_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='order',
            field=models.ManyToManyField(to='hello.Customer'),
        ),
    ]
