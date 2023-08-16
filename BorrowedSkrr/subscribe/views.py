from rest_framework import generics
from .models import Product
from .serializers import ProductListSerializer, ProductRetrieveUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        categoryName = request.GET['category']
        order = request.GET['order']
        # choice에 key 값으로 접근
        query = Product.objects.filter(category=2)
        
        if order == 'basic':
            # Just return the filtered queryset as is
            serializer = self.serializer_class(query, many=True)
        elif order == 'likes':
            # 인기순
            ordered_query = query.order_by('-likes')
            serializer = self.serializer_class(ordered_query, many=True)
        elif order == 'priceLow':
            # 저가순
            ordered_query = query.order_by('priceWeek')
            serializer = self.serializer_class(ordered_query, many=True)
        else:
            # 고가순
            ordered_query = query.order_by('-priceWeek')
            serializer = self.serializer_class(ordered_query, many=True)
        
        return Response(serializer.data)
    

class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveUpdateSerializer
    # permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the instance you want to update
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        instance.likes += 1

        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        
