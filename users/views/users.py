from typing import Any
from django.shortcuts import get_object_or_404
from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import UserModel
from ..serializers.users import (
    CreateUserSerializer,
    ListUserSerializer,
    RetrieveUserSerializer,
)

@extend_schema(tags=["user"])
class UserView(BaseViewSetMixin, ReadOnlyModelViewSet, ListCreateAPIView):
    queryset = UserModel.objects.all()
    lookup_field = "user_id"

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListUserSerializer
            case "retrieve":
                return RetrieveUserSerializer
            case "create":
                return CreateUserSerializer
            case _:
                return ListUserSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()

    def retrieve(self, request, user_id=None):
        user = get_object_or_404(UserModel, user_id=user_id)
        serializer = self.get_serializer(user)
        return Response(serializer.data)
