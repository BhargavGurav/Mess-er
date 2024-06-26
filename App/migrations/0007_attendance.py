# Generated by Django 3.2.2 on 2023-09-22 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_alter_customer_mess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('morning', models.BooleanField()),
                ('evening', models.BooleanField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.customer')),
            ],
        ),
    ]
