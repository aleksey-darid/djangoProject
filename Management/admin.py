from django.contrib import admin

from Management.models import SuppliersModel, ProductionModel, SupplyModel, WagesModel

admin.site.register(SuppliersModel)
admin.site.register(ProductionModel)
admin.site.register(SupplyModel)
admin.site.register(WagesModel)

