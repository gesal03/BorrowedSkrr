from rest_framework import serializers
from .models import Product, Subscribe

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class ProductRetrieveUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    # date = serializers.IntegerField()
    class Meta:
        model = Subscribe
        fields = '__all__'