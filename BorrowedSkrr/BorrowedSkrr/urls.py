from django.contrib import admin
from django.urls import path, include
from subscribe.views import ProductListAPIView, ProductRetrieveUpdateAPIView, SubscribeCreateAPIView,SubscribeUpdateAPIView,MyPageListAPIView, EmpolyeeWishListAPIView,AllowedSubscribeListAPIView, manageStudentAPIView, StudentSubscribeListAPIView, SubscribeRetrieveUpdateAPIView, ReservationCreateAPIView, StudentWishListAPIView, ReservationListAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 제품 List
    path('product/', ProductListAPIView.as_view()),
    # 제품 상세 + 좋아요
    path('product/<int:pk>', ProductRetrieveUpdateAPIView.as_view()),
    # 장바구니 추가
    path('empolyeeShopping', SubscribeCreateAPIView.as_view()),
    # 결제할 상품 List, 결제
    path('subscribe', SubscribeUpdateAPIView.as_view()),
    # 학교 마이페이지 - 메인
    path('schoolMypage/', MyPageListAPIView.as_view()),
    # 학교 마이페이지 - 학생 허가 및 삭제
    path('schoolMypage/manageStudent/<int:pk>', manageStudentAPIView.as_view()),
    # 학교 마이페이지 - 관심 제품
    path('schoolMypage/empolyeeWishList', EmpolyeeWishListAPIView.as_view()),
    # 학교 마이페이지 - 구독 내역
    path('schoolMypage/subscribeList', AllowedSubscribeListAPIView.as_view()),


    # 학생 구독 리스트
    path('student/', StudentSubscribeListAPIView.as_view()),
    # 구독 상세 + 좋아요
    path('student/<int:pk>', SubscribeRetrieveUpdateAPIView.as_view()),
    # 예약
    path('reservation', ReservationCreateAPIView.as_view()),
    # 학생 마이페이지 - 관심 구독
    path('student/studentWishList', StudentWishListAPIView.as_view()),
    # 학생 마이페이지 - 예약 내역
    path('student/reservationList', ReservationListAPIView.as_view()),

    path('accounts/', include('accounts.urls')),
    
]
