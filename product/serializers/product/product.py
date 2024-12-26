from rest_framework import serializers

from ...models import (
    ProductModel,
    CategoryModel,
    ProductImage
)
from product.models.additional import ColorModel, SizeModel, PromotionModel

# -------------------------------
# Individual Field Serializers
# -------------------------------

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'image', 'name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = ['id', 'name', 'image']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = ['id', 'size_name']

# -------------------------------
# Promotion Serializers
# -------------------------------


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionModel
        fields = ['id', 'name']

# -------------------------------
# Product Serializers
# -------------------------------


class ProductListSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True) 

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'main_image', 'price', 'discount_percentage', 'discount_price']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']  


class BaseProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    color = ColorSerializer(many=True, read_only=True)
    size = SizeSerializer(many=True, read_only=True)
    promotion = PromotionSerializer(many=True, read_only=True)
    product_images = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        exclude = [
            "created_at",
            "updated_at",
            'main_image'
        ]

    def get_product_images(self, obj):
        images = ProductImage.objects.filter(product_id=obj.id)
        if not images.exists():
            return []  
        return ProductImageSerializer(images, many=True).data


class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):...


class RetrieveProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):...
        

class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):...
        
