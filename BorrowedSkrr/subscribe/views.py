from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from .models import Product, Shopping, Subscribe, EmpolyeeWishList, Management, Reservation, StudentWishList
from accounts.models import Student
from .serializers import ProductSerializer, SubscribeSerializer, ManagementSerializer, ReservationSerializer, EmpolyeeWishListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# 제품 목록 보여주기, 카테고리 기능
# category = 1,2,3,4
# order = basic, likes, priceLow, priceHigh
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        categoryName = request.GET['category']
        order = request.GET['order']
        # choice에 key 값으로 접근
        query = Product.objects.filter(category=categoryName)
        
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
        instance.likes += 1
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        EmpolyeeWishList(empolyee_id=self.request.user.empolyee.id, product_id=instance)

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
            obj = get_object_or_404(Product, id=subscribe.product_id.id)
            print(obj.count)
            obj.count -= int(subscribe.count)
            obj.save()
            subscribe.save()

        return Response(status=status.HTTP_200_OK)
    
    # # 장바구니 목록 보여주기
    def get_queryset(self):
        queryset = Subscribe.objects.filter(empolyee_id=self.request.user.empolyee.id, isAllowed=False)
        return queryset


# 마이페이지 메인 화면
# 교사 정보 포함 해야됨 - 서영이 코드 받아서 넣기!
class MyPageListAPIView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):

        managementList = Management.objects.filter(empolyee_id = self.request.user.empolyee.id, isAllowed=False)
        reservationList = Reservation.objects.filter(empolyee_id = self.request.user.empolyee.id)

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
        wishListQueryset = EmpolyeeWishList.objects.filter(empolyee_id = self.request.user.empolyee.id)
        queryset=[]
        for item in wishListQueryset:
            obj = get_object_or_404(Product, id=item.product_id.id)
            queryset.append(obj)
        return queryset

# 학교 구독 내역 출력
class AllowedSubscribeListAPIView(generics.ListAPIView):
    serializer_class = SubscribeSerializer

    def get_queryset(self):
        queryset = Subscribe.objects.filter(empolyee_id=self.request.user.empolyee.id, isAllowed=True)
        return queryset

# 학교 학생 관리(허가 및 삭제)
class manageStudentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
    # permission_classes = [IsAuthenticated]

    # 학생 허가
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the instance you want to update
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        instance.isAllowed = True
        student = get_object_or_404(Student, id=instance.student_id.id)
        student.isAllowed = True
        student.save()

        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)
        
    #학생 삭제
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the instance you want to delete
        instance.delete()  # Delete the instance
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# 학생이 속한 학교의 대여 목록
# category = 1,2,3,4
# order = basic, likes, priceLow, priceHigh
class StudentSubscribeListAPIView(generics.ListAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

    def get(self, request, *args, **kwargs):
        # 테스트용
        # user_id = 1
        # 실제 구현 시 이용
        user_id = self.request.user.student.id
        management = Management.objects.filter(student_id = user_id)
        employee_ids = management.values_list('empolyee_id', flat=True)  # Get employee_ids from Management

        subscribe = Subscribe.objects.filter(empolyee_id__in=employee_ids)

        categoryName = request.GET['category']
        subscribe = subscribe.filter(product_id__category=categoryName)
        order = request.GET['order']
        if order == 'basic':
            # Just return the filtered queryset as is
            serializer = self.serializer_class(subscribe, many=True)
        elif order == 'likes':
            # 인기순
            ordered_query = subscribe.order_by('-likes')
            serializer = self.serializer_class(ordered_query, many=True)
        elif order == 'priceLow':
            # 저가순
            ordered_query = subscribe.order_by('-product_id__priceWeek')
            serializer = self.serializer_class(ordered_query, many=True)
        else:
            # 고가순
            ordered_query = subscribe.order_by('-product_id__priceWeek')
            serializer = self.serializer_class(ordered_query, many=True)
        
        return Response(serializer.data)

# 구독 정보 + 학생 좋아요
class SubscribeRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()  # Get the instance you want to update
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        instance.likes += 1
        StudentWishList(student_id=self.request.user.student.id, subscribe_id=instance)

        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data)

# 대여 신청
class ReservationCreateAPIView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def post(self, request, *args, **kwargs):
        subscribe_id = request.data.get('subscribe_id')  # Get the subscribe_id from request data
        count = request.data.get('count')
        try:
            subscribe = Subscribe.objects.get(id=subscribe_id)  # Get the Subscribe object
            subscribe.count -= int(count)
            subscribe.save()
        except Subscribe.DoesNotExist:
            return Response({"error": "Invalid subscribe_id"}, status=status.HTTP_400_BAD_REQUEST)
        
        return self.create(request, *args, **kwargs)

# 학생 관심 목록
class StudentWishListAPIView(generics.ListAPIView):
    serializer_class = SubscribeSerializer

    def get_queryset(self):
        wishListQueryset = StudentWishList.objects.filter(student_id = self.request.user.student.id)
        queryset=[]
        for item in wishListQueryset:
            obj = get_object_or_404(Subscribe, id=item.subscribe_id.id)
            queryset.append(obj)
        return queryset

class ReservationListAPIView(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = Reservation.objects.filter(student_id=self.request.user.student.id)
        return queryset