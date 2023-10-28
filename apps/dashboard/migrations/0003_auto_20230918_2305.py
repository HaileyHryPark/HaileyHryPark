# Generated by Django 2.2.5 on 2023-09-18 15:05

from django.db import migrations

def initialize_location_data(apps, schema_editor):
	location_model = apps.get_model('dashboard','Location')

	location_model.objects.create(
		name = "Korea",
		color = "#0047A0")

	location_model.objects.create(
		name = "Japan",
		color = "#be0029")

	location_model.objects.create(
		name = "United States of America",
		color = "#FFEECC")

	location_model.objects.create(
		name = "Taiwan",
		color = "#FFEECC")

	location_model.objects.create(
		name = "China",
		color = "#FFEECC")

	location_model.objects.create(
		name = "Hong Kong",
		color = "#AE445A")

	location_model.objects.create(
		name = "Czech Republic",
		color = "#AE445A")

	location_model.objects.create(
		name = "Slovenia",
		color = "#AE445A")

	location_model.objects.create(
		name = "Austria",
		color = "#AE445A")

	location_model.objects.create(
		name = "Hungary",
		color = "#AE445A")

	location_model.objects.create(
		name = "Germany",
		color = "#AE445A")

	location_model.objects.create(
		name = "Switzerland",
		color = "#AE445A")

	location_model.objects.create(
		name = "France",
		color = "#AE445A")

	location_model.objects.create(
		name = "United Kingdom",
		color = "#AE445A")

	location_model.objects.create(
		name = "Singapore",
		color = "#A8DF8E")

	location_model.objects.create(
		name = "Vietnam",
		color = "#AE445A")

	location_model.objects.create(
		name = "Spain",
		color = "#FFBFBF")


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20230918_2300'),
    ]

    operations = [
    	migrations.RunPython(initialize_location_data),
    ]