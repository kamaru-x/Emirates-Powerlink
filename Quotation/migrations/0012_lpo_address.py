# Generated by Django 4.2.4 on 2024-03-09 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotation', '0011_lpo_po_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='lpo',
            name='Address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
