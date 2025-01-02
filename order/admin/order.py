from django.contrib import admin
from ..models import OrderModel, OrderItemModel
from unfold.admin import ModelAdmin as UnfoldModelAdmin



@admin.register(OrderItemModel)
class OrderItemAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "order",
        "created_at", 
    )
    
    
    
    
    
class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    extra = 1  
    
    
@admin.register(OrderModel)
class OrderAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at", 
    )
    inlines = [OrderItemInline]


