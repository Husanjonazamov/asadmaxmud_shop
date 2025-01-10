from rest_framework import viewsets
from ..models import CartItemModel
from ..serializers import CreateBasketSerializer, GetBasketSerializers
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import CartItemModel, CartModel
from ..serializers import CreateBasketSerializer, GetBasketSerializers




class BasketView(viewsets.ModelViewSet):
    serializer_class = CreateBasketSerializer
    permission_classes = [AllowAny]
    queryset = CartItemModel.objects.all()

    def perform_create(self, serializer):
        user_id = self.request.data.get("user_id")
        product_id = self.request.data.get("product_id")
        quantity = self.request.data.get("quantity", 1)

        if not user_id:
            raise ValueError("User ID is required.")
        if not product_id:
            raise ValueError("Product ID is required.")

        cart, created = CartModel.objects.get_or_create(user_id=user_id)

        existing_item = CartItemModel.objects.filter(cart=cart, product_id=product_id).first()

        if existing_item:
            existing_item.quantity += int(quantity)
            existing_item.save()
        else:
            serializer.save(cart=cart, product_id=product_id, quantity=quantity)


class GetBasketView(viewsets.ModelViewSet):
    serializer_class = GetBasketSerializers
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')  
        print(user_id)
        if user_id:
            return CartItemModel.objects.filter(cart__user_id=user_id)
        return CartItemModel.objects.none()

    @action(detail=True, methods=["put", "delete"], url_path="item")
    def modify_item(self, request, pk=None, user_id=None):
        try:
            item = CartItemModel.objects.get(cart__user_id=user_id, pk=pk)
        except CartItemModel.DoesNotExist:
            return Response(
                {"detail": "Cart item not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        if request.method == "PUT":
            serializer = self.get_serializer(item, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == "DELETE":
            item.delete()
            return Response(
                {"detail": "Cart item deleted successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )
