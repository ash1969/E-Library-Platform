from django.urls import path
from .views import *

app_name = "ecopysection"
urlpatterns = [
    path('', list_ecopies, name='list_ecopies'),
]