# Generated by Django 3.1.1 on 2020-10-07 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeadmin', '0004_auto_20201007_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='Service_Price',
            new_name='Service_price',
        ),
    ]
