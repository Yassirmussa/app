from django.urls import path

from . import views


urlpatterns=[
    #path("home/",views.hello),
    path("about_us/",views.about),
    path("working_hours/",views.tim),
    #path for addition of number
    path("about_us/add",views.add)
]