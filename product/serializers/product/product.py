from rest_framework import serializers

from ...models import (
    ProductModel,
    CategoryModel,
    ProductImage
)
from product.models.additional import ColorModel, SizeModel, PromotionModel
from django.conf import settings




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



class PromotionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PromotionModel
        fields = ['id', 'name', 'image']



class ProductListSerializer(serializers.ModelSerializer):
    promotion = PromotionSerializer(many=True, read_only=True)
    main_image = serializers.SerializerMethodField()


    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'main_image', 'promotion', 'price', 'discount_percentage', 'discount_price', 'age_group']

    def get_main_image(self, obj):
        request = self.context.get('request')
        if request and obj.main_image:
            return request.build_absolute_uri(obj.main_image.url)
        return None

    
class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        relative_url = f"{settings.MEDIA_URL}{obj.image.name}"
        if request:
            return request.build_absolute_uri(relative_url)
        return relative_url


class BaseProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    color = ColorSerializer(many=True, read_only=True)
    size = SizeSerializer(many=True, read_only=True)
    promotion = PromotionSerializer(many=True, read_only=True)
    product_images = ProductImageSerializer(many=True, read_only=True, source='productimage_set')

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
        
