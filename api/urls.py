from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views.product import ProductView, ProductDetailView, CategoryView
from users.views.users import UserView
from basket.views.basket import BasketView
from order.views.order import OrderView, OrderCreateView

router = DefaultRouter()
# product urls
router.register(r'product', ProductView, basename='product')
router.register(r"product_detail", ProductDetailView, basename='product_detail')

# category urls
router.register(r"category", CategoryView, basename='category')

# users urls
router.register(r"users", UserView, basename='users')

# add urls
router.register(r"cart", BasketView, basename='cart')
router.register(r"order", OrderView, basename='order')
router.register(r"order_create", OrderCreateView, basename='order_create')

urlpatterns = [
    path("", include(router.urls)),
]
