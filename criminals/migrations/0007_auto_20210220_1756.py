# Generated by Django 3.1.6 on 2021-02-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0006_auto_20210220_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminalsinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], default='null', max_length=10),
        ),
    ]
