# Generated by Django 2.2.5 on 2024-06-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20240616_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationinstance',
            name='location_type',
            field=models.CharField(choices=[('t', 'Travel'), ('h', 'Hybrid'), ('l', 'Living'), ('o', 'Other')], default='o', max_length=1),
        ),
    ]