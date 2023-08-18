from django.contrib import admin
from django.urls import path, include
from subscribe.views import ProductListAPIView, ProductRetrieveUpdateAPIView, SubscribeCreateAPIView,SubscribeUpdateAPIView,MyPageManagementListListAPIView, MyPageReservationListAPIView, EmpolyeeWishListAPIView,AllowedSubscribeListAPIView, manageStudentAPIView, StudentSubscribeListAPIView, SubscribeRetrieveUpdateAPIView, ReservationCreateAPIView, StudentWishListAPIView, ReservationListAPIView

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    path('schoolMypageManagement/', MyPageManagementListListAPIView.as_view()),
    path('schoolMypageReservation/', MyPageReservationListAPIView.as_view()),
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
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
