from django.contrib import admin

from ..models import (
    ProductModel,
    CategoryModel,
    ProductImage,
)
from product.models.additional import ColorModel, SizeModel, PromotionModel
from unfold.admin import ModelAdmin as UnfoldModelAdmn



class ProductImageInline(admin.TabularInline): 
    model = ProductImage
    extra = 3

@admin.register(ProductImage)
class ProductImageAdmin(UnfoldModelAdmn):
    list_display = (
        "product",
        "__str__",
    )


@admin.register(CategoryModel)
class CategoryAdmin(UnfoldModelAdmn):
    list_display = (
        "name",
        "__str__",
    )
    
    

@admin.register(ProductModel)
class ProductAdmin(UnfoldModelAdmn):
    list_display = (
        "name",
        "__str__",
    )
    exclude = ('discount_price',)
    inlines = [ProductImageInline]
    
    
                                                                                                                            
@admin.register(SizeModel)
class SizeAdmin(UnfoldModelAdmn):
    list_display = (
        "id",
        "__str__",
    )
    

@admin.register(ColorModel)
class ColorAdmin(UnfoldModelAdmn):
    list_display = (
        "id",
        "__str__",
    )
    
@admin.register(PromotionModel)
class PromotionModelAdmin(UnfoldModelAdmn):
    list_display = (
        "id",
        "__str__",
    )

