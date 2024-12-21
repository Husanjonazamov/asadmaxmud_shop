from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import UserModel
from ..serializers.users import CreateUserSerializer, ListUserSerializer, RetrieveUserSerializer


@extend_schema(tags=["user"])
class UserView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = UserModel.objects.all()

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
