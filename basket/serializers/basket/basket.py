from rest_framework import serializers

from ...models import BasketModel


class BaseBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListBasketSerializer(BaseBasketSerializer):
    class Meta(BaseBasketSerializer.Meta): ...


class RetrieveBasketSerializer(BaseBasketSerializer):
    class Meta(BaseBasketSerializer.Meta): ...


class CreateBasketSerializer(BaseBasketSerializer):
    class Meta(BaseBasketSerializer.Meta): ...
