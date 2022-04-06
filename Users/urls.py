from django.urls import path

from Users.views import user_app, workers_app, login_app, logout_app, registration_app

urlpatterns = [
    path('users_page/', user_app, name="users"),
    path('workers_page/', workers_app, name="workers"),
    path('login_page/', login_app, name="login"),
    path('logout_page/', logout_app, name="logout"),
    path('registration_page/', registration_app, name="registration"),
]
