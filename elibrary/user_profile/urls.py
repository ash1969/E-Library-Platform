from django.urls import path
from .views import *

app_name = "profile"
urlpatterns = [
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
    path('activate/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         activate, name='activate'),
    path('viewProfile/', view_profile, name='view_profile'),
    path('register/', user_register, name="user_register"),
    path('editProfile/', edit_profile, name='edit_profile'),
]