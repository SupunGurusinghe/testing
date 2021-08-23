from django.contrib import admin
from . import models


class SoilAdminArea(admin.AdminSite):
    site_header = 'SOIL ADMIN AREA'
    site_title = 'Soil Management System'


soil_site = SoilAdminArea(name='SoilAdmin')

soil_site.register(models.FertilizerTest)
soil_site.register(models.PlantTermDetails)
soil_site.register(models.LongTermCropDetails)
soil_site.register(models.FertilizerComponents)