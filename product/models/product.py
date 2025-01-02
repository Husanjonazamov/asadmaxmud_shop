from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from decimal import Decimal
from product.models.additional import ColorModel, SizeModel, PromotionModel




class CategoryModel(AbstractBaseModel):
    name = models.CharField(max_length=150, verbose_name=_("Kategoriya nomi"))
    image = models.ImageField(upload_to='category/', verbose_name=_("Kategorya rasmi"))
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"  
        verbose_name = _("Kategoriya")
        verbose_name_plural = _("Kategoriyalar")


class ProductModel(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("Mahsulot nomi"))
    description = models.TextField(verbose_name=_("Tavsif"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Narx"))
    discount_percentage = models.PositiveIntegerField(null=True, blank=True, verbose_name=_("Chegirma foizi"))
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("Chegirma narxi"))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name=_("Kategoriya"))
    color = models.ManyToManyField(ColorModel, verbose_name=_("Ranglar"), related_name="products")  
    main_image = models.ImageField(upload_to="products/", verbose_name=_('Mahsulotning Asosiy Rasmi')) 
    size = models.ManyToManyField(SizeModel, verbose_name=_("O‘lchamlar"), related_name="products")
    promotion = models.ManyToManyField(PromotionModel, verbose_name=_("Aksiyalar"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqti"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Yangilangan vaqti"))
    age_group = models.CharField(max_length=100, verbose_name=_("Yosh chegarasi"), choices=(
        ("all", "Hamma uchun"),
        ("18+", "18 yoshdan katta"),
    ))
    

    
    
    def save(self, *args, **kwargs):
        if self.discount_percentage:
            self.discount_price = self.price * (1 - Decimal(self.discount_percentage) / 100)
        else:
            self.discount_price = self.price 
        super(ProductModel, self).save(*args, **kwargs)


    def __str__(self):
        return self.name or "None"

    class Meta:
        db_table = "product"
        verbose_name = _("Mahsulot")
        verbose_name_plural = _("Mahsulotlar")
        
        
        
        
class ProductImage(AbstractBaseModel):
    image = models.ImageField(upload_to='product_image/', verbose_name=_('Mahsulot Rasmi'))
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name=_('Mahsulot'))
    
    
    class Meta:
        db_table = 'product_image'
        verbose_name = 'Mahsulot Rasmi'
        verbose_name_plural = 'Mahsulot Rasmi'
    
    