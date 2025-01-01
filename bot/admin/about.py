from django.contrib import admin

from ..models import AboutModel, AdvertisingModel
from unfold.admin import ModelAdmin as UnfoldModelAdmin




@admin.register(AboutModel)
class AboutAdmin(UnfoldModelAdmin):
    list_display = (
        "id",
        "__str__",
    )



@admin.register(AdvertisingModel)
class AdvertisingAdmin(UnfoldModelAdmin):
    list_display = (
        'id',
        'name'
    )