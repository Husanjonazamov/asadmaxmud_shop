from django.contrib import admin
from ..models import OrderItemModel, OrderModel
from unfold.admin import ModelAdmin as UnfoldModelAdmin

class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    extra = 1   
    
    

@admin.register(OrderModel)
class OrderAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "name",
        "total_price",  
        "created_at", 
    )
    inlines = [OrderItemInline]
    search_fields = ['name', 'phone']  
    list_filter = ('created_at',)
