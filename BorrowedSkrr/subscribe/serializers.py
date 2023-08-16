from rest_framework import serializers
from .models import Product, Shopping

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class ProductRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ShoppingSerializer(serializers.ModelSerializer):
    # date = serializers.IntegerField()
    class Meta:
        model = Shopping
        fields = '__all__'