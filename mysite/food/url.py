from django.urls import path

from . import views

urlpatterns=[
    path("home/", views.home),
    path("food_registration/", views.foodreg),
    path("list", views.list_food),
    path("customer_Registration", views.customer),
    path("food_order", views.foodorder),
    path("fisherRegisration", views.fishermenreg),
    path("", views.fishers)
]