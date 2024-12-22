from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class UserModel(AbstractBaseModel):
    user_id = models.CharField(unique=True, max_length=155, verbose_name=_('user_id'))
    first_name = models.CharField(max_length=155)
    
    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "user"
        verbose_name = _("Foydalanuvchilar")
        verbose_name_plural = _("Foydalanuvchilar")
