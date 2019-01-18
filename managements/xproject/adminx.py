# -*- coding: utf-8 -*-
# from django.contrib import admin

import xadmin
from .models import *
from xadmin import views
# Register your models here.
#
class GlobalSettings(object):
    site_title = "Wellhotel后台管理系统"
    site_footer = "Wellhotel后台管理系统"
    menu_style = 'accordion'

class basesetting(object):
    enable_themes = True
    use_bootswatch = True

class Subclass_details(object):
    list_display = ('id','name','State','Type','Money','paymenttime')
    list_filter = ['Type']

class Organizations(object):
    list_display = ('id','cname','country','province','city')
    list_filter = ['city']

class DeviceInfos(object):
    list_display = ('id','DeviceID','ADDR','CCID','RegTimes')

xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(views.BaseAdminView,basesetting)
xadmin.site.register(subclass_details,Subclass_details)
xadmin.site.register(Organization,Organizations)
xadmin.site.register(DeviceInfo,DeviceInfos)
# xadmin.site.register(NormalUser)
xadmin.site.register(Price)