from rest_framework import serializers
from product.models.product import ProductModel
from product.models.additional import ColorModel, SizeModel
from users.models.users import UserModel
from ...models import CartItemModel, CartModel
from product.serializers import ProductListSerializer, ColorSerializer, SizeSerializer



class CreateBasketSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all(), source='product', write_only=True)
    color_id = serializers.PrimaryKeyRelatedField(queryset=ColorModel.objects.all(), source='color', write_only=True, required=False)
    size_id = serializers.PrimaryKeyRelatedField(queryset=SizeModel.objects.all(), source='size', write_only=True, required=False)
    quantity = serializers.IntegerField(min_value=1, required=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(), source='user', write_only=True)


    class Meta:
        model = CartItemModel
        fields = ['id', 'product_id', 'color_id', 'size_id', 'user_id', 'quantity']


    def create(self, validated_data):
        product = validated_data.get('product')
        color = validated_data.get('color', None)
        size = validated_data.get('size', None)
        quantity = validated_data.get('quantity')
        user = validated_data.get('user')  

        cart, created = CartModel.objects.get_or_create(user=user)

        cart_item = CartItemModel.objects.create(
            cart=cart,
            product=product,
            color=color,
            size=size,
            quantity=quantity
        )

        return cart_item
    
    
class GetBasketSerializers(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)  
    color = ColorSerializer(read_only=True) 
    size = SizeSerializer(read_only=True) 
    
    class Meta:
        model = CartItemModel
        fields = ['id', 'cart', 'product', 'quantity', 'color', 'size']
    