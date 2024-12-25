from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import OrderItemModel
from ..serializers.order import CreateOrderSerializer, ListOrderSerializer, RetrieveOrderSerializer








@extend_schema(tags=["order"])
class OrderView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = OrderItemModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListOrderSerializer
            case "retrieve":
                return RetrieveOrderSerializer
            case "create":
                return CreateOrderSerializer
            case _:
                return ListOrderSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
