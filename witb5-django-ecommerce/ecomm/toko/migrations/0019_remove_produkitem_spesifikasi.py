# Generated by Django 4.2 on 2023-06-04 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0018_produkitem_spesifikasi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkitem',
            name='spesifikasi',
        ),
    ]
