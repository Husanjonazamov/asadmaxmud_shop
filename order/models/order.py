from django.db import models
from django.utils.translation import gettext_lazy as _
from basket.models.basket import CartItemModel
from django_core.models import AbstractBaseModel
from users.models import UserModel  




class OrderModel(AbstractBaseModel):
    DELIVERY_CHOICES = [
        ('delivery', 'Dostavka'),
        ('pickup', 'Olib Ketish'),
    ]
    PAYMENT = [
        ('cash', "Naqt pul"),
    ]

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_('Foydalanuvchi'))

    basket = models.ManyToManyField(CartItemModel, verbose_name=_("Savat"))
    delivery_type = models.CharField(
        max_length=50,
        choices=DELIVERY_CHOICES,
        default='delivery',
        verbose_name=_('Yetkazib berish turi')
    )
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT,
        default='cash',
        verbose_name=_("To'lov turi")
    )
    name = models.CharField(max_length=255, verbose_name=_('Ism'))
    phone = models.CharField(max_length=20, verbose_name=_('Telefon raqam'))
    address = models.TextField(verbose_name=_('Manzil'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Yaratilgan vaqt'))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Umumiy narx"))

    def __str__(self):
        return f"Buyurtma #{self.id} ({self.name})"

    class Meta:
        db_table = "order"
        verbose_name = _("Buyurtma")
        verbose_name_plural = _("Buyurtmalar")
