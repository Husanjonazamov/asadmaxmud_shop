from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class OrderModel(AbstractBaseModel):
    DELIVERY_CHOICES = [
        ('delivery', 'Dostavka'),
        ('pickup', 'Olib Ketish'),
    ]

    delivery_type = models.CharField(
        max_length=50,
        choices=DELIVERY_CHOICES,
        default='delivery',
        verbose_name=_('Yetkazib berish turi')
    )
    payment_method = models.CharField(
        max_length=50,
        default='Naqd pul', 
        verbose_name=_("To'lov turi")
    )
    name = models.CharField(max_length=255, verbose_name=_('Ism'))
    phone = models.CharField(max_length=20, verbose_name=_('Telefon raqam'))
    address = models.TextField(verbose_name=_('Manzil'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Yaratilgan vaqt'))

    def __str__(self):
        return f"Order by {self.name} ({self.delivery_type})"


    class Meta:
        db_table = "order"
        verbose_name = _("Buyurtma")
        verbose_name_plural = _("Buyurtma")
