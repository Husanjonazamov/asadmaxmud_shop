import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.env import BOT_TOKEN, CHANNEL_ID


def send_telegram_message(order, request):
    bot = telebot.TeleBot(BOT_TOKEN)
    chat_id = CHANNEL_ID
    try:
        user_id = order.user.user_id
        user_info = bot.get_chat(user_id)
    except Exception as e:
        raise Exception(e)
    total_amount = int(sum(item.quantity * item.price for item in order.order_items.all()))

    message_text = (
        f"🛒 Yangi Buyurtma\n"
        f"👤 Mijoz: {order.name}\n"
        f"📞 Telefon: {order.phone}\n"
        f"📞 Telegram: @{user_info.username}\n"
        f"🌆 Shahar: {order.country}\n"
        f"🏠 Manzil: {order.address}\n"
        f"💳 To'lov usuli: {order.payment_method}\n"
        f"🚚 Yetkazib berish usuli: {order.get_delivery_type_display()}\n\n"
        f"💰 Jami Buyurtma Narxi: {total_amount} so'm\n\n"
    )
    
    for item in order.order_items.all():
        item_total_price = int(item.quantity * item.price)  
        message_text += (
            f"📦 Mahsulot: {item.product.name}\n"
            f"🎨 Rang: {item.color.name if item.color else 'Nomaʼlum'}\n"
            f"📏 Oʻlcham: {item.size.size_name if item.size else 'Nomaʼlum'}\n"
            f"🔢 Miqdor: {item.quantity} ta\n"
            f"💵 Birlik Narxi: {int(item.price)} so'm\n"  
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

    inline_keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="✅ Buyrtmani tasdiqlash",
        callback_data=f"check_order_{order.user_id}"  
    )
    inline_keyboard.add(button)
    print(order.user_id)

    if media_files:
        bot.send_media_group(chat_id, media_files)
        # bot.send_message(chat_id, "Buyurtmani Tasdiqlaysizmi ?", reply_markup=inline_keyboard)
    else:
        bot.send_message(chat_id, message_text, reply_markup=inline_keyboard)

    for media in media_files:
        media.media.close()