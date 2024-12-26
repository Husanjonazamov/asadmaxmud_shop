from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views.product import ProductViewSet, ProductDetailView, CategoryView, BannerView
from users.views.users import UserView
from order.views.order import OrderView
from basket.views.basket import BasketView

router = DefaultRouter()
# product urls
router.register(r'products', ProductViewSet, basename='product')
router.register(r"product_detail", ProductDetailView, basename='product_detail')
# router.register(r"init-user", InitUserView, basename='inituser')

# category urls
router.register(r"category", CategoryView, basename='category')

# users urls
router.register(r"users", UserView, basename='users')


# add urls
router.register(r"cart", BasketView, basename='cart')
router.register(r"order", OrderView, basename='order')
router.register(r"banner", BannerView, basename='banner')


urlpatterns = [
    path("", include(router.urls)),
]
