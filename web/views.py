from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.viewsets import ModelViewSet
from web.models import Customer,Order,Product
from api.serializers import ApprovalSerializer
from rest_framework.decorators import action  # Import the 'action' decorator
from rest_framework import generics

  

# Create your views here.
def home(request):
    return render(request,"index.html")


class CheckAuthenticationView(APIView): 
    permission_classes = (IsAuthenticated, )   
    def get(self, request): 
        content = {'message': 'Hello, its Authenticated'} 
        return Response(content) 


class ApprovalViewSet(ModelViewSet):
    queryset = Order.objects.filter(approved=False)
    serializer_class = ApprovalSerializer
    permission_classes = (IsAuthenticated, )   


class ApprovalUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.filter(approved=False)
    serializer_class = ApprovalSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        order_id = self.kwargs['pk']
        return Order.objects.get(pk=order_id)

    def perform_update(self, serializer):
        try:
            instance = serializer.instance
            instance.approved = True  # Set the 'approved' field to True
            Order.objects.filter(pk=instance.pk).update(approved=True)
        except Exception as e:
            print(f"Error updating Order {instance.id}: {e}")
