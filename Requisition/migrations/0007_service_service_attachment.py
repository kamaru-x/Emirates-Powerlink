# Generated by Django 4.2.4 on 2023-12-04 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Requisition', '0006_alter_requisition_requisition_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=225)),
                ('Description', models.TextField(null=True)),
                ('Requisition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Requisition.requisition')),
            ],
        ),
        migrations.CreateModel(
            name='Service_Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attachment', models.FileField(null=True, upload_to='service')),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Requisition.service')),
            ],
        ),
    ]