from django.contrib import admin

from ..models import (
    ProductModel,
    CategoryModel,
    Size,
    Color,
)


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
