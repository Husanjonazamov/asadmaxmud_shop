from typing import Any
from django.shortcuts import get_object_or_404
from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from ..models import UserModel
from ..serializers.users import (
    CreateUserSerializer,
    ListUserSerializer,
    RetrieveUserSerializer,
)


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class InitUserViewSet(viewsets.ViewSet):
    queryset = []  

    def create(self, request):
        try:
            data = request.data
            user_id = data.get("user_id")
            username = data.get("username")

            print(f"Foydalanuvchi ID: {user_id}, Username: {username}")

            return Response(
                {"status": "success", "message": "Foydalanuvchi ma'lumotlari qabul qilindi."},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )




@extend_schema(tags=["user"])
class UserView(BaseViewSetMixin, ViewSet):
    queryset = UserModel.objects.all()
    lookup_field = "user_id"

    def get_serializer_class(self) -> Any:
        """
        Serializerni action-ga qarab tanlash
        """
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
        """
        Permissionslarni action-ga qarab belgilash
        """
        perms = [AllowAny]  
        self.permission_classes = perms
        return super().get_permissions()

    def list(self, request):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, user_id=None):
        user = get_object_or_404(UserModel, user_id=user_id)
        serializer = self.get_serializer(user)
        return Response(serializer.data)

