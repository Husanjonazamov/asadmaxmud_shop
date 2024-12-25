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
        "__str__",
    )
    inlines = [OrderItemInline]


@admin.register(OrderItemModel)
class OrderAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
