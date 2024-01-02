# Generated by Django 4.2.4 on 2024-01-02 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_remove_inventoryitem_inventory_delete_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inventory.inventory_category'),
            preserve_default=False,
        ),
    ]
