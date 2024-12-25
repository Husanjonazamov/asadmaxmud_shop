from rest_framework import serializers
from product.serializers.product.product import ColorSerializer, SizeSerializer, ProductListSerializer

from ...models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # yoki boshqa turdagi maydon
    class Meta:
        model = Cart
        fields = ['user',]


class BaseBasketSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    cart = CartSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)

    class Meta:
        model = CartItem
        exclude = [
            "created_at",
        ]


class ListBasketSerializer(BaseBasketSerializer):
    class Meta(BaseBasketSerializer.Meta): ...


class RetrieveBasketSerializer(BaseBasketSerializer):
    class Meta(BaseBasketSerializer.Meta): ...


class CreateBasketSerializer(BaseBasketSerializer):
    class Meta(BaseBasketSerializer.Meta): ...
