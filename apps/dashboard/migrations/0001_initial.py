# Generated by Django 2.2.5 on 2023-09-18 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=7)),
                ('experience_type', models.CharField(blank=True, choices=[('e', 'Education'), ('w', 'Work'), ('o', 'Other')], default='o', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('experience', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.Experience')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='LocationInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('notes', models.TextField(blank=True, max_length=1000)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_num', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('log', models.TextField(blank=True, max_length=1000)),
                ('experience', models.ManyToManyField(blank=True, to='dashboard.ExperienceInstance')),
                ('location', models.ManyToManyField(blank=True, to='dashboard.LocationInstance')),
            ],
        ),
    ]
