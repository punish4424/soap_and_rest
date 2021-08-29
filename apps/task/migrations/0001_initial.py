# Generated by Django 3.1.1 on 2021-08-27 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fathers_name', models.CharField(max_length=100)),
                ('customer_profile', models.CharField(max_length=100)),
                ('loan_account_number', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='CustomerHomeAddressData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('address3', models.CharField(blank=True, max_length=100, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='task.customer')),
            ],
            options={
                'verbose_name': 'Customer home address',
                'verbose_name_plural': 'Customer home address',
            },
        ),
        migrations.CreateModel(
            name='BranchData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(max_length=100)),
                ('region_name', models.CharField(max_length=100)),
                ('area_name', models.CharField(max_length=100)),
                ('branch_name', models.CharField(max_length=100)),
                ('branch_code', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch_data', to='task.customer')),
            ],
            options={
                'verbose_name': 'Branch data',
                'verbose_name_plural': 'Branch data',
            },
        ),
    ]
