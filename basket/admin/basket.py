from django.contrib import admin

from ..models import BasketModel


@admin.register(BasketModel)
class BasketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
