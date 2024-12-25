from django.contrib import admin

from ..models import Cart, CartItem


@admin.register(Cart)
class BasketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CartItem)
class BasketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
