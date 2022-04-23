from django.urls import path

from Users.views import login_app, logout_app, registration_app, order_app, Workers, users_app, First

workers_crud = Workers()
f = First()
urlpatterns = [
    path('workers_page/', workers_crud.workers_get, name="workers"),
    path('workers_add/', workers_crud.workers_add, name="workers_add"),
    path('workers_del/', workers_crud.workers_del, name="workers_del"),
    path('workers_put/', workers_crud.workers_put, name="workers_put"),
    path('users_page/', users_app, name="users"),
    path('login_page/', login_app, name="login"),
    path('logout_page/', logout_app, name="logout"),
    path('registration_page/', registration_app, name="registration"),
    path('order_page/', order_app, name="order"),
    path('add_all/', f.add_all_first_data, name="add_groops"),

]
