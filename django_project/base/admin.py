from django.contrib.gis import admin
from .models import Location, LocationType

# Register your models here.

admin.site.register(Location, admin.GeoModelAdmin)
admin.site.register(LocationType, admin.GeoModelAdmin)
