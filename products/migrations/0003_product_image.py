# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products-sale'),
        ),
    ]