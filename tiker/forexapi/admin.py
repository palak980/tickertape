from django.contrib import admin
from.models import *
# Register your models here.
@admin.register(Currencies)
class Currencies(admin.ModelAdmin):
    list_display=['currency_name']
