from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class UserModel(AbstractBaseModel):
    user_id = models.CharField(unique=True, max_length=155, verbose_name=_('user_id'))

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "user"
        verbose_name = _("Foydalanuvchilar")
        verbose_name_plural = _("Foydalanuvchilar")
