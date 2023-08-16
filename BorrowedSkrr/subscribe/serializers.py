from rest_framework import serializers
from .models import Product

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class ProductRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'