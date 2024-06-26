# Generated by Django 3.2.2 on 2023-09-14 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20230908_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mess', models.CharField(max_length=50)),
                ('registration', models.DateField()),
                ('contact', models.CharField(max_length=15)),
                ('type', models.CharField(max_length=10)),
                ('per_month', models.IntegerField()),
            ],
        ),
    ]
