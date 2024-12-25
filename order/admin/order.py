from django.contrib import admin

from ..models import OrderModel
from unfold.admin import ModelAdmin as UnfoldModelAdmn



@admin.register(OrderModel)
class OrderAdmin(UnfoldModelAdmn):
    list_display = (
        "id",
        "__str__",
    )
