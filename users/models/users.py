from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel

    

class UserModel(AbstractBaseModel):
    user_id = models.CharField(unique=True, max_length=155, verbose_name=_('user_id'), null=True, blank=True)
    name = models.CharField(max_length=155, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True) 
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "user"
        verbose_name = _("Foydalanuvchilar")
        verbose_name_plural = _("Foydalanuvchilar")
    
    def save(self, *args, **kwargs):
        self.pk = self.user_id
        super().save(*args, **kwargs)
