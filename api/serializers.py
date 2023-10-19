from web.models import Customer,Order,Product
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'phone', 'birth_date','user' ]



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField()
    total_amount = serializers.IntegerField(read_only=True)  # Mark the field as read-only


    class Meta:
        model = Order
        fields = ['user', 'product', 'quantity', 'total_amount', 'approved']



class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','approved','user', 'product','total_amount',]


