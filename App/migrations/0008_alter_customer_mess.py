# Generated by Django 3.2.2 on 2023-09-23 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mess',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.messowner'),
        ),
    ]
