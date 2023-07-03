# Generated by Django 4.1.5 on 2023-07-03 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0005_voter_title'),
        ('school_admin', '0008_alter_title_date'),
        ('candidate', '0002_candidates_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.candidates')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_admin.positions')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voter.voter')),
            ],
            options={
                'db_table': 'votes_db',
            },
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.candidates')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_admin.positions')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voter.voter')),
            ],
            options={
                'db_table': 'votes_tb',
            },
        ),
    ]