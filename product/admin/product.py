from django.contrib import admin

from ..models import (
    ProductModel,
    CategoryModel,
    ProductImage,
)
from product.models.additional import ColorModel, SizeModel, PromotionModel, BannerModel
from unfold.admin import ModelAdmin as UnfoldModelAdmn

# ----------------------
# Inlines
# ----------------------


class ProductImageInline(admin.TabularInline): 
    model = ProductImage
    extra = 3

# ----------------------
# Product
# ----------------------


@admin.register(ProductModel)
class ProductAdmin(UnfoldModelAdmn):
    list_display = (
        'id',
        "name",
        "__str__",
    )
    exclude = ('discount_price',)
    inlines = [ProductImageInline]
    
    filter_horizontal = ('color', 'size', 'promotion')
    
    

# ----------------------
# Category
# ----------------------




@admin.register(CategoryModel)
class CategoryAdmin(UnfoldModelAdmn):
    list_display = (
        'id',
        "name",
        "__str__",
    )
    
    
# ----------------------
# Size va color
# ----------------------

    

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
    

# ----------------------
#  Promotion
# ----------------------

    
    
@admin.register(PromotionModel)
class PromotionModelAdmin(UnfoldModelAdmn):
    list_display = (
        "id",
        "__str__",
    )


# ----------------------
#  Banner
# ----------------------



@admin.register(BannerModel)
class BannerModelAdmin(UnfoldModelAdmn):
    list_display = (
        "id",
        "__str__"
    )