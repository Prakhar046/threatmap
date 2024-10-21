# Generated by Django 3.2.25 on 2024-09-30 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threat_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('threat_level', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('reported', models.DateTimeField(auto_now_add=True)),
                ('origin', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('attack_destination', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'threatcollection',
            },
        ),
    ]