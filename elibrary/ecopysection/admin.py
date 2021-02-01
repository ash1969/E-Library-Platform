from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(ECopies)
class ECopiesAdmin(admin.ModelAdmin):
    pass
