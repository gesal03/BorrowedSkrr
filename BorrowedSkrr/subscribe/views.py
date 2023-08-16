from rest_framework import generics
from .models import Product, Shopping, Subscribe, EmpolyeeWishList
from .serializers import ProductListSerializer, ProductRetrieveUpdateSerializer, SubscribeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# 제품 목록 보여주기, 카테고리 기능
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
    

# get: 상품 상세 정보, patch: 좋아요 기능(likes 증가, EmpolyeeWishList 추가)
class ProductRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveUpdateSerializer
    # permission_classes = [IsAuthenticated]

    # 좋아요
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the instance you want to update
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        instance.likes += 1
        EmpolyeeWishList(empolyee_id=self.request.user.id, product_id=instance)

        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)

# 장바구니 목록 보여주기(isAllowed=False), 장바구니 추가
class SubscribeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SubscribeSerializer

    # 장바구니 목록 보여주기
    def get_queryset(self):
        user_id = self.request.user.id
        query = Subscribe.objects.filter(empolyee_id=user_id, isAllowed=False)
        return query

# 결제하기
class SubscribeUpdateAPIView(generics.UpdateAPIView, generics.ListAPIView):
    serializer_class = SubscribeSerializer

    def patch(self, request, *args, **kwargs):
        # Get the queryset
        queryset = Subscribe.objects.filter(empolyee_id=request.user.id, isAllowed=False)

        for subscribe_obj in queryset:
            subscribe_obj.isAllowed = True
            subscribe_obj.save()

        return Response(self.get_serializer(queryset, many=True).data)
    
    def get_queryset(self):
        queryset = Subscribe.objects.filter(empolyee_id=self.request.user.id, isAllowed=False)
        serializer = self.serializer_class(queryset, many=True)
        return queryset

class SubscribeCreateAPIView(generics.CreateAPIView):
    queryset = Subscribe.objects.all()
    # serializer_class = 
