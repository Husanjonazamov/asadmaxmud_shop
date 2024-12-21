from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from product.models.product import ProductModel


class BasketModel(AbstractBaseModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name=_('Mahsulot nomi'))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Miqdori"))
    added_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Qo‘shilgan vaqti"))


    def __str__(self):
        return f"Savat: {self.product.name} ({self.quantity} dona)"

    class Meta:
        db_table = "basket"
        verbose_name = _("Savat")
        verbose_name_plural = _("Savat")
