# your_project/your_app/authentication.py
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models.users import UserModel
    
class TelegramAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Foydalanuvchining Telegram user_id sini olish
        user_id = request.headers.get('Telegram-User-ID')
        if user_id is None:
            return None  # Agar headerda 'Telegram-User-ID' bo'lmasa, autentifikatsiya o'tkazilmaydi

        try:
            user = UserModel.objects.get(user_id=user_id)  # Telegram user_id orqali foydalanuvchini topish
        except UserModel.DoesNotExist:
            raise AuthenticationFailed('Foydalanuvchi topilmadi.')

        # Foydalanuvchini qaytarish
        return (user, None)  # Foydalanuvchi va None, chunki bizda parol yo'q
