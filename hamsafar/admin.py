from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Trip)
class Admin(admin.ModelAdmin):
    list_display = ("driver","start_location")
    list_filter=("driver","start_location")
    

admin.site.register(Request),
admin.site.register(Application),
