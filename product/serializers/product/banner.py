from rest_framework import serializers
from product.models.additional import BannerModel



class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = ['id', 'name', 'image',]
        
