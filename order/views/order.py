from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from ..models import OrderModel
from ..serializers.order import BaseOrderSerializer


@extend_schema(tags=["order"])
class OrderView(ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = BaseOrderSerializer
    permission_classes = [AllowAny]
