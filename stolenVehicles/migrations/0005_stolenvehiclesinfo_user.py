# Generated by Django 3.1.6 on 2021-02-20 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stolenVehicles', '0004_stolenvehiclesinfo_admin_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='stolenvehiclesinfo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
