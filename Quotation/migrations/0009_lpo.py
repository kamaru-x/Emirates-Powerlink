# Generated by Django 4.2.4 on 2023-11-17 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quotation', '0008_quotation_lpo_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='LPO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TRN', models.CharField(max_length=25, null=True)),
                ('PO_Date', models.DateField(null=True)),
                ('Reference', models.CharField(max_length=50, null=True)),
                ('Payment_Terms', models.TextField(null=True)),
                ('Delivery_Terms', models.TextField(null=True)),
                ('Terms_Condetions', models.TextField(null=True)),
                ('Contact', models.CharField(max_length=50, null=True)),
                ('Delivery_Location', models.CharField(max_length=50, null=True)),
                ('Remarks', models.CharField(max_length=255, null=True)),
                ('Payment_Mode', models.CharField(max_length=50, null=True)),
                ('Delivery_Date', models.DateField(null=True)),
                ('Order_Date', models.DateField(null=True)),
                ('Quotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quotation.quotation')),
            ],
        ),
    ]