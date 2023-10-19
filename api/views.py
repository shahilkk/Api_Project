from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from web.models import Customer,Order,Product
from .serializers import CustomerSerializer,OrderSerializer,ProductSerializer
from rest_framework.decorators import action  
from rest_framework.response import Response
  

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        total_amount = product.price * quantity

        if total_amount >= 50000:
            serializer.validated_data['approved'] = False
        else:
            serializer.validated_data['approved'] = True

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
    


    