# Generated by Django 2.2.5 on 2024-06-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20240616_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experienceinstance',
            name='experience_type',
            field=models.CharField(choices=[('w', 'Work'), ('e', 'Education'), ('o', 'Other')], default='o', max_length=1),
        ),
        migrations.AlterField(
            model_name='locationinstance',
            name='location_type',
            field=models.CharField(choices=[('t', 'Travel'), ('h', 'Hybrid'), ('l', 'Living'), ('o', 'Other')], default='o', max_length=1),
        ),
    ]
