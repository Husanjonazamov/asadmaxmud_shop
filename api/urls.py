from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views.product import ProductView, ProductDetailView
from users.views.users import UserView


router = DefaultRouter()
router.register(r'product', ProductView, basename='product')
router.register(r"product_detail", ProductDetailView, basename='product_detail')
router.register(r"users", UserView, basename='users')





urlpatterns = [
    path("", include(router.urls)),
]
