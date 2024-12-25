from django.contrib import admin

from ..models import OrderItemModel, OrderModel
from unfold.admin import ModelAdmin as UnfoldModelAdmin


@admin.register(OrderModel)
class OrderAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(OrderItemModel)
class OrderAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
