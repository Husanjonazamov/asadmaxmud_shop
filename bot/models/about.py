from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel




class AboutModel(AbstractBaseModel):
    description = models.TextField(verbose_name=_('Malumot kiriting'))

    def __str__(self):
        return self.description[0:3]

    @classmethod
    def _create_face(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "about"
        verbose_name = _("Bot haqida Malumot")
        verbose_name_plural = _("Bot haqida Malumot")



class AdvertisingModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("Reklama nomi"), max_length=100)
    video = models.FileField(upload_to='ads_video/', verbose_name=_('Reklama videosini kiriting'))
    video_link = models.CharField(max_length=100, verbose_name=_("Video Linki"), null=True, blank=True)
    is_activate = models.BooleanField(default=True, help_text="Reklama faoligini belgilang")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    @classmethod
    def _create_face(self):
        return self.objects.create(
            name="Test",
        )
        
    class Meta:
        db_table = 'Advertising'
        managed = True
        verbose_name = 'Reklama'
        verbose_name_plural = 'Reklama'
    
    