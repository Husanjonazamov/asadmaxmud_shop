from rest_framework import serializers
from product.serializers.product.product import ColorSerializer, SizeSerializer, ProductListSerializer
from ...models import OrderModel, OrderItemModel


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)

    class Meta:
        model = OrderItemModel
        fields = ['id', 'product', 'quantity', 'color', 'size', 'price']
        # fields = '__all__'


class CreateOrderItemSeralizer(serializers.Serializer):
    product = ProductListSerializer(read_only=True)
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)

    class Meta:
        model = OrderItemModel
        fields = ['product', 'quantity', 'color', 'size', 'price']


class CreateOrderModelSerializer(serializers.ModelSerializer):
    items = CreateOrderItemSeralizer(many=True)

    class Meta:
        model = OrderModel
        fields = ['delivery_type', 'payment_method', 'name', 'phone', 'address', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = OrderModel.objects.create(**validated_data)
        for item_data in items_data:
            product = item_data.get('product')
            if not product:
                raise serializers.ValidationError("Product must be provided for ishlamayapti")
            OrderItemModel.objects.create(order=order, **item_data)
        return order


class BaseOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = OrderModel
        fields = ['id', 'delivery_type', 'payment_method', 'name', 'phone', 'address', 'created_at', 'total_price',
                  'items']


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...
