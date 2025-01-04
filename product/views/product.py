from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import ProductModel, CategoryModel, BannerModel
from ..serializers.product import (
        ProductListSerializer,
        CategorySerializer,
        BaseProductSerializer
    )
from ..serializers.product import BannerSerializers
from django.db.models import Q
from django_core.paginations import CustomPagination



class ProductViewSet(ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.query_params.get('category_name', None)

        if category_name:
            queryset = queryset.filter(Q(category__name__icontains=category_name))  
        return queryset


class CategoryView(ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    
    
class ProductDetailView(ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = BaseProductSerializer


class BannerView(ReadOnlyModelViewSet):
    queryset = BannerModel.objects.all()
    serializer_class = BannerSerializers
    






