from rest_framework import serializers
from product.serializers.product.product import ColorSerializer, SizeSerializer, ProductListSerializer
from ...models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # fields = ['name','phone', 'address', 'total_price']
        fields = '__all__'


class BaseOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    product = ProductListSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)

    class Meta:
        model = OrderItem
        exclude = []


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...
