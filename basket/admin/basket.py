from django.contrib import admin

from ..models import CartModel, CartItemModel
from unfold.admin import ModelAdmin as  UnfoldModelAdmin



@admin.register(CartModel)
class BasketAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CartItemModel)
class BasketAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
