# Generated by Django 4.2.4 on 2023-11-13 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Requisition', '0004_requisition_item_reference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisition_item',
            name='Reference',
        ),
    ]
