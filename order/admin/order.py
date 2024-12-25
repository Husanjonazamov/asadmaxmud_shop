from django.contrib import admin

from ..models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
