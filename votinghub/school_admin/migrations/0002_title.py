# Generated by Django 4.1.5 on 2023-06-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'title_tb',
            },
        ),
    ]