from rest_framework import serializers
from .models import Empolyee, Student, User
from django.contrib.auth import authenticate
from django.utils import timezone

class EmpolyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empolyee
        fields = ('school', 'certificate')

class StudentSerializer(serializers.ModelSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username', 'name', 'password')

class EmpolyeeUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Empolyee
        fields = ('user', 'school', 'certificate')


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username = user_data['username'],
            name = user_data['name'],
            password = user_data['password']
        )
        # user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        empolyee, created = Empolyee.objects.update_or_create(user=user,
                        school=validated_data.pop('school'),
                        certificate=validated_data.pop('certificate'))
        return empolyee


class StudentUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Student
        fields = ('user', 'subscribeCode', 'grade', 'classNumber','number')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(
            username = user_data['username'],
            name = user_data['name'],
            password = user_data['password']
        )
        # user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = Student.objects.update_or_create(user=user,
                        subscribeCode=validated_data.pop('subscribeCode'),
                        grade=validated_data.pop('grade'),
                        classNumber=validated_data.pop('classNumber'),
                        number=validated_data.pop('number'))
        return student

# 아이디, 패스워드, 이름 변경 불가
class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ['user']

# 아이디, 패스워드, 이름 변경 불가
class EmployeeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empolyee
        exclude = ['user']

