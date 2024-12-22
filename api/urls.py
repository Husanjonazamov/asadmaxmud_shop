from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views.product import ProductView, ProductDetailView, CategoryView
from users.views.users import UserView


router = DefaultRouter()
# product urls
router.register(r'product', ProductView, basename='product')
router.register(r"product_detail", ProductDetailView, basename='product_detail')

# category urls
router.register(r"category", CategoryView, basename='category')

# users urls
router.register(r"users", UserView, basename='users')





urlpatterns = [
    path("", include(router.urls)),
]
