from rest_framework import serializers

from ...models import AboutModel, AdvertisingModel



class AdvertisingSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingModel
        fields = ['id', 'name', 'video', 'video_link']



class BaseAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListAboutSerializer(BaseAboutSerializer):
    class Meta(BaseAboutSerializer.Meta): ...


class RetrieveAboutSerializer(BaseAboutSerializer):
    class Meta(BaseAboutSerializer.Meta): ...


class CreateAboutSerializer(BaseAboutSerializer):
    class Meta(BaseAboutSerializer.Meta): ...
