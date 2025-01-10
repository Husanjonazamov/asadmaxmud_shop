from rest_framework import serializers
from order.models import OrderModel, OrderItemModel
from product.serializers import ProductListSerializer, ProductImageSerializer, ColorSerializer, SizeSerializer
from order.views.order_send import send_telegram_message
from product.serializers import ProductListSerializer, ProductImageSerializer, ColorSerializer, SizeSerializer
from basket.models import CartItemModel, CartModel


class GetOrderItemSerializers(serializers.ModelSerializer):
    product = ProductListSerializer()
    color = ColorSerializer()
    size = SizeSerializer()

    class Meta:
        model = OrderItemModel
        fields = ['product', 'color', 'size', 'quantity', 'price']




class GetListOrderSerializers(serializers.ModelSerializer):
    order_items = GetOrderItemSerializers(many=True)
    class Meta:
        model = OrderModel
        fields = ['user', 'delivery_type', 'payment_method', 'name', 'phone', 'country', 'address', 'order_items']



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        fields = ['product', 'color', 'size', 'quantity', 'price']



class ListOrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    class Meta:
        model = OrderModel
        fields = ['user', 'delivery_type', 'payment_method', 'name', 'phone', 'country', 'address', 'order_items']



class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.ListField(
        child=OrderItemSerializer(),
        required=False  
    )

    class Meta:
        model = OrderModel
        fields = ['user', 'delivery_type', 'payment_method', 'name', 'phone', 'country', 'address', 'order_items']

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
                
            user = validated_data.get('user')   
            cart = CartModel.objects.filter(user=user).first()
            if cart:
                for item_data in order_items_data:
                    product = item_data.get('product')
                    CartItemModel.objects.filter(cart=cart, product=product).delete()

            send_telegram_message(order, request=request)

            return order
        except Exception as e:
            print(f"Xatolik: {e}")  
            raise e


