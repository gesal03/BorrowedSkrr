from django.contrib import admin
from django.urls import path
from subscribe.views import ProductListAPIView, ProductRetrieveUpdateAPIView, SubscribeCreateAPIView,SubscribeUpdateAPIView,MyPageListAPIView, EmpolyeeWishListAPIView,AllowedSubscribeListAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    # 제품 List
    path('product/', ProductListAPIView.as_view()),
    # 제품 상세
    path('product/<int:pk>', ProductRetrieveUpdateAPIView.as_view()),
    # 장바구니 추가
    path('shopping', SubscribeCreateAPIView.as_view()),
    # 결제할 상품 List, 결제
    path('subscribe', SubscribeUpdateAPIView.as_view()),
    # 학교 마이페이지 - 메인
    path('schoolMypage/', MyPageListAPIView.as_view()),
    # 학교 마이페이지 - 관심 제품
    path('schoolMypage/empolyeeWishList', EmpolyeeWishListAPIView.as_view()),
    # 학교 마이페이지 - 구독 내역
    path('schoolMypage/subscribeList', AllowedSubscribeListAPIView.as_view())
]
