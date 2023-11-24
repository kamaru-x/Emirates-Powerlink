# Generated by Django 4.2.4 on 2023-11-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('U_Auth', '0003_alter_user_job_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Job_Role',
            field=models.CharField(choices=[('Department Manager', 'Department Manager'), ('Project Engineer', 'Project Engineer'), ('Purchase Manager', 'Purchase Manager'), ('Site Engineer', 'Site Engineer'), ('Accountant', 'Accountant'), ('Developer', 'Developer'), ('Super Admin', 'Super Admnin')], max_length=25, null=True),
        ),
    ]