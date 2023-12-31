# Generated by Django 4.2.4 on 2023-11-10 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.IntegerField(default=1)),
                ('Project_Status', models.IntegerField(default=0)),
                ('Added_Date', models.DateField(auto_now_add=True)),
                ('Added_IP', models.GenericIPAddressField(null=True)),
                ('Edited_Date', models.DateField(null=True)),
                ('Edited_IP', models.GenericIPAddressField(null=True)),
                ('Client_Name', models.CharField(max_length=100)),
                ('Client_Mobile', models.CharField(max_length=15, null=True)),
                ('Client_Email', models.EmailField(max_length=254, null=True)),
                ('Client_Address', models.TextField(null=True)),
                ('Contact_Name', models.CharField(max_length=100, null=True)),
                ('Contact_Number', models.CharField(max_length=15, null=True)),
                ('Expected_Starting_Date', models.DateField(null=True)),
                ('Expected_Amount', models.FloatField(null=True)),
                ('Added_By', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_created', to=settings.AUTH_USER_MODEL)),
                ('Department_Managers', models.ManyToManyField(related_name='Department_Managers', to=settings.AUTH_USER_MODEL)),
                ('Edited_By', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_edited', to=settings.AUTH_USER_MODEL)),
                ('Project_Engineers', models.ManyToManyField(related_name='Project_Engineers', to=settings.AUTH_USER_MODEL)),
                ('Purchase_Managers', models.ManyToManyField(related_name='Purchase_Managers', to=settings.AUTH_USER_MODEL)),
                ('Site_Engineers', models.ManyToManyField(related_name='Site_Engineers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
