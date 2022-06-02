# Generated by Django 4.0.4 on 2022-05-27 17:30

import ckeditor.fields
import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('h_name', models.CharField(max_length=100)),
                ('address', ckeditor.fields.RichTextField()),
                ('district', models.CharField(choices=[('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Kannur', 'Kannur'), ('Trivandrum', 'Trivandrum'), ('Palakkad', 'Palakkad'), ('Thrissur', 'Thrissur'), ('Kottayam', 'Kottayam'), ('Alappuzha', 'Alappuzha'), ('Idukki', 'Idukki'), ('Kollam', 'Kollam'), ('Ernakulam', 'Ernakulam'), ('Wayanad', 'Wayanad'), ('Kasaragod', 'Kasaragod'), ('Pathanamthitta', 'Pathanamthitta')], max_length=50)),
                ('state', models.CharField(choices=[('kerala', 'kerala'), ('demo', 'demo')], max_length=50)),
                ('contact', models.BigIntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('date_of_joined', models.DateTimeField(default=datetime.datetime(2022, 5, 27, 22, 59, 59, 671808))),
                ('h_image', cloudinary.models.CloudinaryField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
