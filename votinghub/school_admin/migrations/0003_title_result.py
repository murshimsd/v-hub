# Generated by Django 4.1.5 on 2023-07-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_admin', '0002_title_date_alter_title_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='result',
            field=models.CharField(default='not-published', max_length=50),
        ),
    ]