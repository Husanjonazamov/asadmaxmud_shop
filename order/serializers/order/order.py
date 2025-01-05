from rest_framework import serializers
from order.models import OrderModel, OrderItemModel
from product.serializers import ProductListSerializer, ProductImageSerializer, ColorSerializer, SizeSerializer
from order.views.order_send import send_telegram_message
from django.conf import settings




from django.conf import settings
from rest_framework import serializers

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()
    color = ColorSerializer()
    size = SizeSerializer()

    class Meta:
        model = OrderItemModel
        fields = ['product', 'color', 'size', 'quantity', 'price']



class ListOrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = OrderModel
        fields = ['user', 'delivery_type', 'payment_method', 'name', 'phone', 'address', 'order_items']



class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.ListField(
        child=OrderItemSerializer(),
        required=False  
    )

    class Meta:
        model = OrderModel
        fields = ['user', 'delivery_type', 'payment_method', 'name', 'phone', 'address', 'order_items']

    def create(self, validated_data):
        request = self.context.get('request')
        
        if not request:
            raise ValueError("Request object not found in serializer context.")
        
        try:
            order_items_data = validated_data.pop('order_items', [])
            order = OrderModel.objects.create(**validated_data)

            for item_data in order_items_data:
                item_data['order'] = order
                OrderItemModel.objects.create(**item_data)

            send_telegram_message(order, request=request)

            return order
        except Exception as e:
            print(f"Xatolik: {e}")  
            raise e


