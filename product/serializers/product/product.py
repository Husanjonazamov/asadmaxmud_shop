from rest_framework import serializers

from ...models import ProductModel


class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class RetrieveProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...
