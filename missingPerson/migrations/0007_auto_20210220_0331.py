# Generated by Django 3.1.6 on 2021-02-19 22:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('missingPerson', '0006_auto_20210220_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingpersoninfo',
            name='datetime',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
