# Generated by Django 4.2.4 on 2024-01-26 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_sub_category_sub_in_category_product_sub_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='Core.category'),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='Core.category'),
        ),
    ]