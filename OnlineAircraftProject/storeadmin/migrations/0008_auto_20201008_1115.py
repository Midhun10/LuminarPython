# Generated by Django 3.1.1 on 2020-10-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeadmin', '0007_manufacture_manufacture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftmodels',
            name='Aircraft_image',
            field=models.ImageField(default='None', upload_to=''),
        ),
        migrations.AlterField(
            model_name='manufacture',
            name='Manufacture_image',
            field=models.ImageField(default='None', upload_to=''),
        ),
    ]
