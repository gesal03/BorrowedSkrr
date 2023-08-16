from django.contrib import admin
from django.urls import path
from subscribe.views import ProductListAPIView, ProductRetrieveUpdateAPIView, ShoppingCreateAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>', ProductRetrieveUpdateAPIView.as_view()),
    path('shopping', ShoppingCreateAPIView.as_view()),
]
