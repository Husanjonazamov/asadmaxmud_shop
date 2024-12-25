from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import ProductModel, CategoryModel, BannerModel
from ..serializers.product import (
        ProductListSerializer,
        CategorySerializer,
        BaseProductSerializer
    )
from ..serializers.product import BannerSerializers




class ProductView(ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductListSerializer



class CategoryView(ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    

    
class ProductDetailView(ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = BaseProductSerializer


class BannerView(ReadOnlyModelViewSet):
    queryset = BannerModel.objects.all()
    serializer_class = BannerSerializers
    






