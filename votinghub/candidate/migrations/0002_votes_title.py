# Generated by Django 4.1.5 on 2023-07-06 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_admin', '0002_title_date_alter_title_status'),
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='title',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='school_admin.title'),
        ),
    ]
