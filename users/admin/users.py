from django.contrib import admin

from ..models import UserModel
from unfold.admin import ModelAdmin as UnfoldModelAdmin 


@admin.register(UserModel)
class UserAdmin(UnfoldModelAdmin):
    list_display = (
        'id',
        "user_id",
        "__str__",
    )
