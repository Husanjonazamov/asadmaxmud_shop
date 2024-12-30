from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from ..serializers.order import CreateOrderSerializer
from ..models import OrderModel
from ..serializers.order import BaseOrderSerializer


class OrderCreateView(ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = CreateOrderSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=["order"])
class OrderView(ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = BaseOrderSerializer
    permission_classes = [AllowAny]
