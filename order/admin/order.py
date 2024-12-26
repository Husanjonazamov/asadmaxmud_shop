from django.contrib import admin
from ..models import OrderModel
from unfold.admin import ModelAdmin as UnfoldModelAdmin


@admin.register(OrderModel)
class OrderAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "name",
        "total_price",  
        "created_at", 
    )
