from typing import Any
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..models import UserModel
from ..serializers.users import CreateUserSerializer, ListUserSerializer, RetrieveUserSerializer



@extend_schema(tags=["user"])
class UserView(ModelViewSet):
    queryset = UserModel.objects.all()
    lookup_field = "user_id" 

    def get_serializer_class(self) -> Any:
        """
        Serializerni action-ga qarab tanlash
        """
        if self.action == 'list':
            return ListUserSerializer
        elif self.action == 'retrieve':
            return RetrieveUserSerializer
        elif self.action == 'create':
            return CreateUserSerializer
        return ListUserSerializer

    def get_permissions(self) -> Any:
        """
        Permissionslarni action-ga qarab belgilash
        """
        self.permission_classes = [AllowAny]
        return super().get_permissions()
