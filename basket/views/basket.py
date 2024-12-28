from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import CartItemModel
from ..serializers import CreateBasketSerializer, GetBasketSerializers

class BasketView(viewsets.ModelViewSet):
    serializer_class = CreateBasketSerializer
    permission_classes = [IsAuthenticated]

    queryset = CartItemModel.objects.all()
    
    def perform_create(self, serializer):
        user_id = self.request.data.get('user_id') 
        serializer.save(cart__user_id=user_id)  
        
        
        
class GetBaskerView(viewsets.ModelViewSet):
    serializer_class = GetBasketSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')  
        print(f"User ID: {user_id}") 
        if user_id:
            return CartItemModel.objects.filter(cart__user_id=user_id)  
        return CartItemModel.objects.none() 