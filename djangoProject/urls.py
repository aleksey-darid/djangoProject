"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

import Administration.urls
import Management.urls
import Users.urls
from Administration.views import ScheduleView, BidView
from Management.views import ProductionView, SuppliersView, SupplyView
from Users.views import home_app, UserView

router = SimpleRouter()
router.register("api/supply", SupplyView)
router.register("api/suppliers", SuppliersView)
router.register("api/production", ProductionView)
router.register("api/bid", BidView)
router.register('api/user', UserView)
router.register("api/schedule", ScheduleView)

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include(Management.urls)),
    path('', include(Administration.urls)),
    path('', include(Users.urls)),
    path('', home_app, name='home'),
]
urlpatterns += router.urls
