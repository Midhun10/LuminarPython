# Generated by Django 3.1.1 on 2020-10-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeadmin', '0008_auto_20201008_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraftmodels',
            name='Aircraft_image',
            field=models.ImageField(default='None', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='manufacture',
            name='Manufacture_image',
            field=models.ImageField(default='None', upload_to='images'),
        ),
    ]