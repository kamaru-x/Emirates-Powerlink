# Generated by Django 4.2.4 on 2023-11-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotation', '0004_alter_quotationitem_net_alter_quotationitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='Note',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
