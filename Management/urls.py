from django.urls import path

from Management.views import supply_app, production_app, wages_app, Sup_app, Suppliers

urlpatterns = [
    path('supply_page/', supply_app, name="supply"),
    path('suppliers_page/', Suppliers.suppliers_get, name="suppliers_get"),
    path('production_page/', production_app, name="production"),
    path('wages_page/', wages_app, name="wages"),
    path('sup/', Sup_app),
    path('suppliers_del/', Suppliers.suppliers_del, name="suppliers_del"),
    path('suppliers_add/', Suppliers.suppliers_add, name="suppliers_add"),
    path('suppliers_put/', Suppliers.suppliers_put, name="suppliers_put"),
]

