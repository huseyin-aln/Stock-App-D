# Generated by Django 4.1.1 on 2022-10-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_firm_created_firm_updated_product_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='price_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8),
        ),
    ]
