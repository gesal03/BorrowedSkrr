from .serializers import StudentUserSerializer, StudentInfoSerializer, EmployeeInfoSerializer,EmpolyeeUserSerializer
from .models import Empolyee, Student
from rest_framework import generics

# 교직원 회원가입
class EmpolyeeCreate(generics.CreateAPIView):
    queryset = Empolyee.objects.all()
    serializer_class = EmpolyeeUserSerializer

# 학생 회원가입
class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentUserSerializer

class StudentInfoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentInfoSerializer

class EmployeeInfoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empolyee.objects.all()
    serializer_class = EmployeeInfoSerializer

