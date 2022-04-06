from django.urls import path

from Management.views import supply_app, suppliers_app, production_app, wages_app, Sup_app

urlpatterns = [
    path('supply_page/', supply_app, name="supply"),
    path('suppliers_page/', suppliers_app, name="suppliers"),
    path('production_page/', production_app, name="production"),
    path('wages_page/', wages_app, name="wages"),
    path('sup/', Sup_app),
]

