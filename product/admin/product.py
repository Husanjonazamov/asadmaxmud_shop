from django.contrib import admin

from ..models import (
    ProductModel,
    CategoryModel,
    ProductImage,
    Size,
    Color,
)


class ProductImageInline(admin.TabularInline): 
    model = ProductImage
    extra = 3

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "__str__",
    )
    
    


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "__str__",
    )
    
    

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "__str__",
    )
    inlines = [ProductImageInline]
    
    

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
