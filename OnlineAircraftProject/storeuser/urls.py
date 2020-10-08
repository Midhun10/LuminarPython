from storeuser.views import home
from django.urls import path, include
from storeadmin.views import index

urlpatterns = [
    path("", home, name="home"),
    path("adminhome", index, name="adminhome")
]
