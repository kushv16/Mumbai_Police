# Generated by Django 3.1.6 on 2021-02-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0005_auto_20210216_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintsinfo',
            name='crime',
            field=models.CharField(choices=[('cyber', 'Cyber'), ('extortion', 'Extortion'), ('chain snatching', 'Chain Snatching'), ('dacotiy', 'Dacoity'), ('theft', 'Theft'), ('others', 'Others')], default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='complaintsinfo',
            name='desc',
            field=models.CharField(default='null', max_length=250),
        ),
    ]