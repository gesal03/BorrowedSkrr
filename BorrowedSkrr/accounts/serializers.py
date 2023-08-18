from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Empolyee, Student, User
from subscribe.models import Management
import random
import string

def randomStr():
    n=10	# 문자의 개수(문자열의 크기)
    rand_str = ""	# 문자열

    for i in range(n):
        rand_str += str(random.choice(string.ascii_letters + string.digits))
    return rand_str

class EmpolyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empolyee
        fields = ('school', 'certificate')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

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
            password = user_data['password'],
        )
        # user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        empolyee, created = Empolyee.objects.update_or_create(user=user,
                        school=validated_data.pop('school'),
                        certificate=validated_data.pop('certificate'))
        empolyee.schoolCode = randomStr()
        empolyee.save()
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
        empolyee = get_object_or_404(Empolyee, schoolCode = student.subscribeCode)
        management = Management(empolyee_id=empolyee, student_id = student)
        management.save()
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

