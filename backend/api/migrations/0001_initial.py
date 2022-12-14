# Generated by Django 4.0.6 on 2022-07-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('FName', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=20)),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField()),
                ('Category', models.CharField(max_length=10)),
                ('Ward', models.CharField(max_length=50)),
                ('SubDistrict', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=25)),
                ('Pincode', models.IntegerField()),
                ('Mobile', models.BigIntegerField()),
                ('AadharNo', models.BigIntegerField()),
                ('Disablity', models.CharField(max_length=3)),
                ('DisabilityType', models.TextField()),
                ('BPL_Family_ID', models.CharField(max_length=50)),
                ('BankDetails', models.TextField()),
            ],
        ),
    ]
