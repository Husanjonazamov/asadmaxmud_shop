from django.contrib import admin

from ..models import BasketModel
from unfold.admin import ModelAdmin as UnfoldModelAdmin 

@admin.register(BasketModel)
class BasketAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
