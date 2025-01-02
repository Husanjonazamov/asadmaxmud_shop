from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel



class ColorModel(AbstractBaseModel):
    COLOR_CHOICES = [
        ("Ko'k", "Ko'k"),
        ('Qizil', 'Qizil'),
        ('Qora', 'Qora'),
        ('Yashil', 'Yashil'),
        ('Oq', 'Oq'),
        ('Sariq', 'Sariq'),
        ('Kulrang', 'Kulrang'),
        ('Jigarrang', 'Jigarrang'),
        ('Pushti', 'Pushti'),
        ('Siyohrang', 'Siyohrang'),
    ]
    name = models.CharField(max_length=55, choices=COLOR_CHOICES, verbose_name=_('nomini kiriting'))
    image = models.ImageField(upload_to='color/', verbose_name=_("Rang tasviri"))

    def __str__(self):
        return self.name or "None"

    class Meta:
        db_table = "color"  
        verbose_name = _("Rang")
        verbose_name_plural = _("Ranglar")



class SizeModel(AbstractBaseModel):
    size_name = models.CharField(max_length=50, verbose_name=_("O‘lcham nomi"))

    def __str__(self):
        return self.size_name or "None"

    class Meta:
        db_table = "size"  
        verbose_name = _("O‘lcham")
        verbose_name_plural = _("O‘lchamlar")
        
        
        
class PromotionModel(AbstractBaseModel):
    name = models.CharField(max_length=100, verbose_name=_("Aksiya nomi"))
    image = models.ImageField(upload_to='promotion_image/', verbose_name=_("Rasmni kiriting"))
    
    def __str__(self):
        return self.name or "None"
    
    class Meta:
        db_table = "promotion"
        verbose_name = _('Aksiyalar')
        verbose_name_plural = 'Aksiyalar'
    
        
        
        
class BannerModel(AbstractBaseModel):
    name = models.CharField(max_length=200, verbose_name=_("Banner nomi"))
    image = models.ImageField(upload_to="banner/", verbose_name=_("Banner Rasmi"))
    
    
    def __str__(self):
        return self.name or "None"
    
    class Meta:
        db_table = 'banner'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banner'