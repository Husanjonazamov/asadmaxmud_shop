from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import AboutModel, AdvertisingModel
from ..serializers.about import CreateAboutSerializer, ListAboutSerializer, RetrieveAboutSerializer, AdvertisingSerializers



class AdvertisingView(ReadOnlyModelViewSet):
    queryset = AdvertisingModel.objects.filter(is_activate=True)
    serializer_class = AdvertisingSerializers




@extend_schema(tags=["about"])
class AboutView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = AboutModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListAboutSerializer
            case "retrieve":
                return RetrieveAboutSerializer
            case "create":
                return CreateAboutSerializer
            case _:
                return ListAboutSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
