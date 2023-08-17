from rest_framework import serializers
from .models import Product, Subscribe, Management, Reservation, EmpolyeeWishList
from accounts.serializers import StudentSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 


class SubscribeSerializer(serializers.ModelSerializer):
    product = ProductSerializer(source='product_id', read_only=True)
    class Meta:
        model = Subscribe
        fields = '__all__'

class ManagementSerializer(serializers.ModelSerializer):
    student = StudentSerializer(source='student_id')
    class Meta:
        model = Management
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class EmpolyeeWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpolyeeWishList
        fields = '__all__'