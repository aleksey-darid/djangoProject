from django.urls import path

from Administration.views import bid_app, schedule_app

urlpatterns = [
    path('bid_page/', bid_app, name="bid"),
    path('schedule_page/', schedule_app, name="schedule"),
]
