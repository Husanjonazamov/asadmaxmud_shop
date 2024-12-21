from rest_framework import serializers

from ...models import OrderModel


class BaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...
