from django.contrib import admin

from Administration.models import ScheduleModel, BidModel

admin.site.register(ScheduleModel)
admin.site.register(BidModel)