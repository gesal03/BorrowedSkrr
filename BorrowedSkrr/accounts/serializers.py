from rest_framework import serializers
from .models import Empolyee, Student, User
from django.contrib.auth import authenticate
from django.utils import timezone

class EmpolyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empolyee
        fields = ['school', 'certificate']

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['username', 'name', 'password']

class EmployeeUserSerializer(serializers.ModelSerializer):
    school = serializers.CharField()
    certificate = serializers.ImageField()
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        Empolyee.objects.create(user=user, school=validated_data['school'], certificate=validated_data['certificate'])
        return user
    class Meta:
        model = User
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     student = Student.objects.create_student(
    #         name = validated_data['name'],
    #         username = validated_data['username'],
    #         password = validated_data['password'],
    #         password2 = validated_data['password2'],
    #         subscribeCode = validated_data['subscribeCode'],
    #         grade = validated_data['grade'],
    #         classNumber = validated_data['classNumber'],
    #         number = validated_data['number'],
    #     )
    #     return student
    class Meta:
        model = Student
        fields = '__all__'


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class EmployeeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empolyee
        fields = '__all__'

