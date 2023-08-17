from django.contrib.auth import authenticate

from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from .serializers import EmpolyeeSerializer, StudentSerializer
from .models import Empolyee, Student
from rest_framework import generics



# 교직원 회원가입
class EmpolyeeCreate(generics.CreateAPIView):
    queryset = Empolyee.objects.all()
    serializer_class = EmpolyeeSerializer

# 학생 회원가입
class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password, )
    if user:
        token, _  = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response(status=401)
