# serializers.py

from rest_framework import serializers
import requests
from decimal import Decimal
from ...models import OrderModel, CartItemModel
from utils.env import BOT_TOKEN, CHANNEL_ID




class OrderItemModelSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    product_image = serializers.ImageField(source="product.main_image", read_only=True)
    color = serializers.CharField(source="color.name", read_only=True)
    size = serializers.CharField(source="size.name", read_only=True)

    class Meta:
        model = CartItemModel
        fields = ['product_name', 'product_image', 'quantity', 'color', 'size', 'total_price']



class BaseOrderSerializer(serializers.ModelSerializer):
    items = OrderItemModelSerializer(many=True, read_only=True)  # CartItemModelni Order modelida ko'rsatish
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)  # Umumiy narx

    class Meta:
        model = OrderModel
        fields = ['id', 'user', 'basket', 'delivery_type', 'payment_method', 'name', 'phone', 'address', 'created_at', 'total_price', 'items']
        read_only_fields = ['id', 'created_at', 'total_price', 'items']

    def create(self, validated_data):
        # request'dan foydalanuvchining ma'lumotlarini olish
        user = self.context['request'].user
        validated_data['user'] = user  # validated_data ga userni qo'shish

        # Orderni yaratish
        order = super().create(validated_data)

        # Telegram'ga buyurtma yuborish
        self.send_order_to_telegram(order)

        return order

    def send_order_to_telegram(self, order):
        """Telegram API orqali buyurtma ma'lumotlarini yuborish"""
        token = BOT_TOKEN
        chat_id = CHANNEL_ID
        
        url = f"https://api.telegram.org/bot{token}/sendMessage"

        # Xabarni tayyorlash
        message = f"\ud83d\uded2 <b>Buyurtma #{order.id}</b>\n"
        message += f"\ud83d\udcde <b>Telefon:</b> {order.phone}\n"
        message += f"\ud83d\udccd <b>Manzil:</b> {order.address}\n"
        message += f"\ud83d\ude9a <b>Yetkazib berish turi:</b> {order.delivery_type}\n"
        message += f"\ud83d\udcb3 <b>To'lov turi:</b> {order.payment_method}\n"
        message += f"\ud83d\udcb0 <b>Umumiy narx:</b> {order.total_price} so'm\n\n"
        message += "\ud83d\udce6 <b>Buyurtma mahsulotlari:</b>\n"

        for item in order.items.all():
            product_image_url = item.product.main_image.url if item.product.main_image else "Rasm yo'q"
            message += f"\u2022 <b>Mahsulot:</b> {item.product.name}\n"
            message += f"  \ud83c\udfa8 <b>Rang:</b> {item.color}\n"
            message += f"  \ud83d\udd22 <b>O'lcham:</b> {item.size}\n"
            message += f"  \ud83d\udcb8 <b>Narxi:</b> {item.total_price} so'm\n"
            message += f"  \ud83d\uddbc <b>Rasm:</b> {product_image_url}\n\n"

        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }

        response = requests.post(url, data=payload)

        if response.status_code == 200:
            print("✅ Xabar muvaffaqiyatli yuborildi!")
        else:
            print(f"❌ Xato: {response.status_code}, {response.text}")
