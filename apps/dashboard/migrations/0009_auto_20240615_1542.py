# Generated by Django 2.2.5 on 2024-06-15 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='location',
            field=models.ManyToManyField(blank=True, to='dashboard.LocationInstance'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
