from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from .models import Product, Shopping, Subscribe, EmpolyeeWishList, Management, Reservation
from .serializers import ProductSerializer, SubscribeSerializer, ManagementSerializer, ReservationSerializer, EmpolyeeWishListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# 제품 목록 보여주기, 카테고리 기능
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
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
    serializer_class = ProductSerializer
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

# 장바구니 추가
class SubscribeCreateAPIView(generics.CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

    # # 장바구니 목록 보여주기
    # def get_queryset(self):
    #     user_id = self.request.user.id
    #     query = Subscribe.objects.filter(empolyee_id=user_id, isAllowed=False)
    #     return query

# 장바구니 목록 보여주기(isAllowed=False), 결제하기
class SubscribeUpdateAPIView(generics.UpdateAPIView, generics.ListAPIView):
    serializer_class = SubscribeSerializer

    def update(self, request, *args, **kwargs):
        filtered_subscribes = Subscribe.objects.filter(isAllowed=False)  # Filter objects with isAllowed=False
        
        for subscribe in filtered_subscribes:
            subscribe.isAllowed = True
            subscribe.save()

        return Response(status=status.HTTP_200_OK)
    
    # # 장바구니 목록 보여주기
    def get_queryset(self):
        queryset = Subscribe.objects.filter(empolyee_id=self.request.user.id, isAllowed=False)
        return queryset


# 마이페이지 메인 화면
# 교사 정보 포함 해야됨 - 서영이 코드 받아서 넣기!
class MyPageListAPIView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):

        managementList = Management.objects.filter(empolyee_id = self.request.user.id, isAllowed=False)
        reservationList = Reservation.objects.filter(empolyee_id = self.request.user.id)

        managementSerializer = ManagementSerializer(managementList, many=True)
        reservationSerializer = ReservationSerializer(reservationList, many=True)

        content = {
            "management": managementSerializer.data,
            "reservation": reservationSerializer.data
        }

        return Response(content)

# 학교 위시 리스트 출력
class EmpolyeeWishListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        wishListQueryset = EmpolyeeWishList.objects.filter(empolyee_id = self.request.user.id)
        queryset=[]
        for item in wishListQueryset:
            obj = get_object_or_404(Product, id=item.product_id.id)
            queryset.append(obj)
        return queryset

class AllowedSubscribeListAPIView(generics.ListAPIView):
    serializer_class = SubscribeSerializer

    def get_queryset(self):
        queryset = Subscribe.objects.filter(empolyee_id=self.request.user.id, isAllowed=True)
        return queryset