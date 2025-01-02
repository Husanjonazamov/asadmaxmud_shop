import telebot
from utils.env import BOT_TOKEN, CHANNEL_ID


def send_telegram_message(order, request):
    bot = telebot.TeleBot(BOT_TOKEN)
    chat_id = CHANNEL_ID

    # Hisoblangan umumiy narxni topamiz va butun son sifatida ko'rsatamiz
    total_amount = int(sum(item.quantity * item.price for item in order.order_items.all()))

    message_text = (
        f"🛒 Yangi Buyurtma\n"
        f"👤 Mijoz: {order.name}\n"
        f"📞 Telefon: {order.phone}\n"
        f"🏠 Manzil: {order.address}\n"
        f"💳 To'lov usuli: {order.payment_method}\n"
        f"🚚 Yetkazib berish usuli: {order.delivery_type}\n\n"
        f"💰 Jami Buyurtma Narxi: {total_amount} so'm\n\n"
    )
    
    # Buyurtma detallari
    for item in order.order_items.all():
        item_total_price = int(item.quantity * item.price)  # Jami narxni butun son sifatida
        message_text += (
            f"📦 Mahsulot: {item.product.name}\n"
            f"🎨 Rang: {item.color.name if item.color else 'Nomaʼlum'}\n"
            f"📏 Oʻlcham: {item.size.size_name if item.size else 'Nomaʼlum'}\n"
            f"🔢 Miqdor: {item.quantity} ta\n"
            f"💵 Birlik Narxi: {int(item.price)} so'm\n"  # Birlik narxni butun son sifatida
            f"💸 Jami Narx (mahsulot): {item_total_price} so'm\n\n"
        )

    media_files = []
    i = True
    for item in order.order_items.all():
        if item.product.main_image:
            image_path = item.product.main_image.path
            if i:
                media_files.append(
                    telebot.types.InputMediaPhoto(open(image_path, 'rb'), caption=message_text)
                )
                i = False
            else:
                media_files.append(
                    telebot.types.InputMediaPhoto(open(image_path, 'rb'))
                )

    if media_files:
        bot.send_media_group(chat_id, media_files)

    print("Xabar va rasmlar muvaffaqiyatli yuborildi.")

    # Fayllarni yopishni unutmang
    for media in media_files:
        media.media.close()
