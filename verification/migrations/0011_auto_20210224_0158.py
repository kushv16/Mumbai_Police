# Generated by Django 3.1.6 on 2021-02-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0010_verificationinfo_admin_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationinfo',
            name='desc',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='propOwnerAddress',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='propOwnerCity',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='propOwnerContact',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='propOwnerCountry',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='propOwnerEmail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='propOwnerFlatno',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='propOwnerFullName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='propOwnerState',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantAddress',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantBranch',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantCity',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantContact',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantCountry',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantDepartment',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantEmail',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantFlatno',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantFullName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantID',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantInstitute',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantOrganisation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantReason',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='verificationinfo',
            name='tenantState',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
