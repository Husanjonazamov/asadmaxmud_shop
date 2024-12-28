from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from product.models.product import ProductModel
from users.models.users import UserModel
from product.models.additional import ColorModel, SizeModel
from decimal import Decimal


class CartModel(AbstractBaseModel):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name=_("Foydalanuvchi"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))

    def __str__(self):
        return f"Savat #{self.id} ({self.user})"

    class Meta:
        db_table = "cart"
        verbose_name = _("Savat")
        verbose_name_plural = _("Savatchalar")



class CartItemModel(AbstractBaseModel):
    cart = models.ForeignKey('CartModel', related_name="items", on_delete=models.CASCADE, verbose_name=_("Savat"))
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name=_("Mahsulot"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Miqdor"))
    color = models.ForeignKey(ColorModel, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("Rang"))
    size = models.ForeignKey(SizeModel, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("O‘lcham"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))

    @property
    def total_price(self):
        return Decimal(self.quantity) * Decimal(self.product.discount_price or self.product.price)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    class Meta:
        db_table = "cart_item"
        verbose_name = _("Savatdagi Mahsulot")
        verbose_name_plural = _("Savatdagi Mahsulotlar")
