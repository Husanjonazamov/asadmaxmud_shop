from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from decimal import Decimal



class CategoryModel(AbstractBaseModel):
    name = models.CharField(max_length=150, verbose_name=_("Kategoriya nomi"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"  
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")



class Color(models.Model):
    image = models.ImageField(upload_to='color/', verbose_name=_("Rang tasviri"))

    class Meta:
        db_table = "color"  
        verbose_name = _("Rang")
        verbose_name_plural = _("Ranglar")



class Size(models.Model):
    size_name = models.CharField(max_length=50, verbose_name=_("O‘lcham nomi"))

    def __str__(self):
        return self.size_name

    class Meta:
        db_table = "size"  
        verbose_name = _("O‘lcham")
        verbose_name_plural = _("O‘lchamlar")
        
        
        

class ProductModel(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Mahsulot nomi"))
    description = models.TextField(verbose_name=_("Tavsif"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Narx"))
    discount_percentage = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Chegirma foizi"))
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("Chegirma narxi"))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name=_("Kategoriya"))
    color = models.ManyToManyField(Color, verbose_name=_("Ranglar"), related_name="products")  # related_name belgilandi
    size = models.ManyToManyField(Size, verbose_name=_("O‘lchamlar"), related_name="products")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))
    


    def save(self, *args, **kwargs):
        if self.discount_percentage:
            self.discount_price = self.price * (1 - Decimal(self.discount_percentage) / 100)
        else:
            self.discount_price = self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = _("Mahsulot")
        verbose_name_plural = _("Mahsulotlar")
