from django.contrib import admin
from .models import *
# Register your models here.
#
admin.site.register(subclass_details)
admin.site.register(Organization)
admin.site.register(DeviceInfo)
admin.site.register(NormalUser)
admin.site.register(Price)