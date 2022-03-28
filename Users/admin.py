from django.contrib import admin

from Users.models import WorkersModel, OrderModel, ManagerModel

admin.site.register(WorkersModel)
admin.site.register(OrderModel)
admin.site.register(ManagerModel)
