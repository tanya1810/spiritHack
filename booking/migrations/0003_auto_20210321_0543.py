# Generated by Django 3.1.7 on 2021-03-21 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20210321_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booked_time', to='booking.time'),
        ),
    ]