# Generated by Django 4.1.5 on 2023-06-20 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_admin', '0004_positions_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='positions',
            name='password',
        ),
    ]