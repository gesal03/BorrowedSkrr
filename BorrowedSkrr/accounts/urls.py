from django.urls import path, include
from . import views
from rest_framework import urls


urlpatterns = [
    #path('signup/', include('dj_rest_auth.registration.urls')),
    path('employee-signup/', views.EmpolyeeCreate.as_view()),
    path('student-signup/', views.StudentCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
