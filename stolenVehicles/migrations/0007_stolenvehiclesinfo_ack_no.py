# Generated by Django 3.1.6 on 2021-02-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stolenVehicles', '0006_stolenvehiclesinfo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='stolenvehiclesinfo',
            name='ack_no',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]