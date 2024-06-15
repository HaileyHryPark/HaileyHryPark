from django.contrib import admin
from .models import Week, Location, LocationInstance, ExperienceInstance

# Register your models here.
admin.site.register(Week)
admin.site.register(Location)
admin.site.register(LocationInstance)
admin.site.register(ExperienceInstance)