# Generated by Django 4.2.4 on 2023-11-15 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Requisition', '0006_alter_requisition_requisition_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vendor', models.CharField(max_length=100)),
                ('Requisition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Requisition.requisition')),
            ],
        ),
    ]