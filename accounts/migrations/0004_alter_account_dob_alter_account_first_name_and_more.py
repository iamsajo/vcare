# Generated by Django 4.0.4 on 2022-05-27 10:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_account_district_account_dob_account_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 15, 30, 50, 262493)),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
