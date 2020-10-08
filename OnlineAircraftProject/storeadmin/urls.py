from storeadmin.views import index, manufactureCreate, aircraftCreate, serviceCreate, manufactureEdit, manufactureView, \
    manufactureDelete, aircraftEdit, aircraftView, aircraftDelete, serviceEdit, serviceDelete
from storeuser.views import home
from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("manufacture", manufactureCreate, name="manufacture"),
    path("aircraft", aircraftCreate, name="aircraft"),
    path("service", serviceCreate, name="service"),
    path("manufactureedit/<int:pk>", manufactureEdit, name="editmanufacture"),
    path("manufactureview/<int:pk>", manufactureView, name="viewmanufacture"),
    path("deletemanufacture/<int:pk>", manufactureDelete, name="deletemanufacture"),
    path("aircraftedit/<int:pk>", aircraftEdit, name="editaircraft"),
    path("aircraftview/<int:pk>", aircraftView, name="viewaircraft"),
    path("deleteaircraft/<int:pk>", aircraftDelete, name="deleteaircraft"),
    path("editservice/<int:pk>", serviceEdit, name="editservice"),
    path("deleteservice", serviceDelete, name="deleteservice"),
    path("userhome",home,name="userhome")
]
