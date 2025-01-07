from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db import transaction
from ..models import OrderModel, OrderItemModel
from ..serializers import OrderSerializer, ListOrderSerializer, GetListOrderSerializers



class UserOrdersView(APIView):
    permission_classes = [AllowAny]
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        orders = OrderModel.objects.filter(user__id=user_id)

        if not orders.exists():
            return Response({"message": "Buyurtmalar topilmadi."}, status=404)

        serializer = GetListOrderSerializers(orders, many=True, context={'request': request})
        return Response(serializer.data)



class OrderView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        orders = OrderModel.objects.all()
        serializer = ListOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = OrderSerializer(data=data, context={'request': request}) 

        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"detail": "created"})
            except Exception as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(
                {"errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
