from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from product.models.product import ProductModel
from product.models.additional import SizeModel, ColorModel


class Order(models.Model):
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
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_("Umumiy narx"))


    def calculate_total_price(self):
        self.total_price = sum(item.total_price() for item in self.items.all())
        self.save()

    def __str__(self):
        return f"Buyurtma #{self.id} ({self.name})"

    class Meta:
        db_table = "order"
        verbose_name = _("Buyurtma")
        verbose_name_plural = _("Buyurtmalar")

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE, verbose_name=_("Buyurtma"))
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name=_("Mahsulot"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Miqdor"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Narx"))
    color = models.ForeignKey(ColorModel, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("Rang"))
    size = models.ForeignKey(SizeModel, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_("O‘lcham"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqt"))
    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    class Meta:
        db_table = "order_item"
        verbose_name = _("Buyurtmadagi Mahsulot")
        verbose_name_plural = _("Buyurtmadagi Mahsulotlar")
