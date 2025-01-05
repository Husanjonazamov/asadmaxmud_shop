from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views.product import ProductViewSet, ProductDetailView, CategoryView, BannerView
from users.views.users import UserView
from order.views.order import OrderView, UserOrdersView
from basket.views.basket import GetBasketView, BasketView
from bot.views import AboutView, AdvertisingView



router = DefaultRouter()
# product urls
router.register(r'products', ProductViewSet, basename='product')
router.register(r"product_detail", ProductDetailView, basename='product_detail')
# router.register(r"init-user", InitUserView, basename='inituser')
router.register(r'cart/(?P<user_id>\d+)', GetBasketView, basename='t')

# category urls
router.register(r"category", CategoryView, basename='category')

# users urls
router.register(r"users", UserView, basename='users')

# add urls
router.register(r"cart", BasketView, basename='cart')
router.register(r"banner", BannerView, basename='banner')
router.register(r"about", AboutView, basename='about')
router.register(r"advertising", AdvertisingView, basename='advertising')



urlpatterns = [
    path("", include(router.urls)),
    path("order/", OrderView.as_view(), name='order'),
    path("order/<int:user_id>/", UserOrdersView.as_view(), name='getusers'),
]
