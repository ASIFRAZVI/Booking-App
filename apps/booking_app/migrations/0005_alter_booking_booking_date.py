# Generated by Django 5.0.7 on 2024-08-04 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0004_booking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(),
        ),
    ]