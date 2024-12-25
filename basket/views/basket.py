from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import CartItem
from ..serializers.basket import CreateBasketSerializer, ListBasketSerializer, RetrieveBasketSerializer


@extend_schema(tags=["basket"])
class BasketView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CartItem.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListBasketSerializer
            case "retrieve":
                return RetrieveBasketSerializer
            case "create":
                return CreateBasketSerializer
            case _:
                return ListBasketSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
