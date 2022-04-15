from django.urls import path

from Management.views import production_app, wages_app, Sup_app, Suppliers, Supply, look_order_app, look_bid_app

suppliers_crud = Suppliers()
supply_crud = Supply()
urlpatterns = [
    path('supply_page/', supply_crud.supply_get, name="supply_get"),
    path('supply_add/', supply_crud.supply_add, name="supply_add"),
    path('supply_del/', supply_crud.supply_del, name="supply_del"),
    path('supply_put/', supply_crud.supply_put, name="supply_put"),
    path('suppliers_page/', suppliers_crud.suppliers_get, name="suppliers_get"),
    path('suppliers_del/', suppliers_crud.suppliers_del, name="suppliers_del"),
    path('suppliers_add/', suppliers_crud.suppliers_add, name="suppliers_add"),
    path('suppliers_put/', suppliers_crud.suppliers_put, name="suppliers_put"),
    path('production_page/', production_app, name="production"),
    path('look_order_page/', look_order_app, name="look_order"),
    path('look_bid_page/', look_bid_app, name="look_bid"),
    path('wages_page/', wages_app, name="wages"),
    path('sup/', Sup_app),

]

