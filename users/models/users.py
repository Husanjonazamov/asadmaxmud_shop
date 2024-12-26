from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
import uuid




class UserModel(AbstractBaseModel):
    user_id = models.CharField(unique=True, max_length=155, verbose_name=_('user_id'))
    first_name = models.CharField(max_length=155)
    token = models.CharField(max_length=255, unique=True, blank=True, null=True, verbose_name=_("Token"))

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = str(uuid.uuid4()) 
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name


    class Meta:
        db_table = "user"
        verbose_name = _("Foydalanuvchilar")
        verbose_name_plural = _("Foydalanuvchilar")
