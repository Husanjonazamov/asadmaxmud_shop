from rest_framework import serializers

from ...models import (
    ProductModel,
    CategoryModel,
    Color,
    Size,
    ProductImage
)

# -------------------------------
# Individual Field Serializers
# -------------------------------

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'image', 'name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'image']


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'size_name']


# -------------------------------
# Product Serializers
# -------------------------------

class ProductListSerializer(serializers.ModelSerializer):
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
    product_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = ProductModel
        exclude = [
            "created_at",
            "updated_at",
            'main_image'
        ]


class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):...


class RetrieveProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):...
        


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):...
        
