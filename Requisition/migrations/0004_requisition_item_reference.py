# Generated by Django 4.2.4 on 2023-11-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Requisition', '0003_requisition_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisition_item',
            name='Reference',
            field=models.CharField(default='RI-000', max_length=50),
            preserve_default=False,
        ),
    ]