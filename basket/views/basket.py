from typing import Any

from django_core.mixins import BaseViewSetMixin
from typing import Any
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from ..models import CartModel, CartItemModel
from ..serializers.basket import CreateBasketSerializer
from product.models.product import ProductModel
from product.models.additional import ColorModel, SizeModel
from users.models.users import UserModel

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated




class BasketView(viewsets.ModelViewSet):
    queryset = CartItemModel.objects.all()
    permission_classes = [IsAuthenticated]  

    def get_serializer_class(self):
        return CreateBasketSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


