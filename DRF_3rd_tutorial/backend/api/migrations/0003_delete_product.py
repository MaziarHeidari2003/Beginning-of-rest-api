# Generated by Django 5.0 on 2024-05-02 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]