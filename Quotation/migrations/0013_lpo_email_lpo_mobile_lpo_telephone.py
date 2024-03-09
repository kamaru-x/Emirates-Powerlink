# Generated by Django 4.2.4 on 2024-03-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotation', '0012_lpo_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='lpo',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='lpo',
            name='Mobile',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='lpo',
            name='Telephone',
            field=models.CharField(max_length=25, null=True),
        ),
    ]