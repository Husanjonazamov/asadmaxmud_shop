from rest_framework import serializers
from product.serializers.product.product import ColorSerializer, SizeSerializer, ProductListSerializer
from ...models import CartModel, CartItemModel
from product.models.product import ProductModel
from product.models.additional import ColorModel, SizeModel
from users.models.users import UserModel

class CreateBasketSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    color = ColorSerializer(read_only=True, required=False)
    size = SizeSerializer(read_only=True, required=False)

    product_id = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all(), write_only=True)
    color_id = serializers.PrimaryKeyRelatedField(queryset=ColorModel.objects.all(), required=False, write_only=True)
    size_id = serializers.PrimaryKeyRelatedField(queryset=SizeModel.objects.all(), required=False, write_only=True)
    quantity = serializers.IntegerField(min_value=1, required=True)

    class Meta:
        model = CartItemModel
        fields = ['product_id', 'color_id', 'size_id', 'quantity', 'product', 'color', 'size']

    def create(self, validated_data):
        product = validated_data.pop('product_id')
        color = validated_data.pop('color_id', None)
        size = validated_data.pop('size_id', None)
        quantity = validated_data.pop('quantity')

        # Tekshirish: request.user autentifikatsiyadan o'tgan bo'lishi kerak
        user = self.context['request'].user
        if not isinstance(user, UserModel):
            raise serializers.ValidationError("Foydalanuvchi autentifikatsiya qilinmagan.")

        # Savatni yoki foydalanuvchi uchun yangi savat yaratish
        cart, created = CartModel.objects.get_or_create(user=user)

        # CartItemModel yaratish
        cart_item = CartItemModel.objects.create(
            cart=cart,
            product=product,
            color=color,
            size=size,
            quantity=quantity
        )
        return cart_item
