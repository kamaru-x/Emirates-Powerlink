# Generated by Django 4.2.4 on 2023-11-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotation', '0009_lpo'),
    ]

    operations = [
        migrations.AddField(
            model_name='lpo',
            name='PO_Category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lpo',
            name='Q_Reference',
            field=models.CharField(max_length=25, null=True),
        ),
    ]