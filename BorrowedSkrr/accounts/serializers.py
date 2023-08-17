from rest_framework import serializers
from .models import Empolyee, Student
from django.contrib.auth import authenticate
from django.utils import timezone

class EmpolyeeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        empolyee = Empolyee.objects.create_empolyee(
            name = validated_data['name'],
            username = validated_data['username'],
            password = validated_data['password'],
            password2 = validated_data['password2'],
            school = validated_data['school'],
            certificate = validated_data['certificate'],
        )
        return empolyee
    class Meta:
        model = Empolyee
        fields = ['name', 'username', 'password', 'password2', 'school', 'certificate']

class StudentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        student = Student.objects.create_student(
            name = validated_data['name'],
            username = validated_data['username'],
            password = validated_data['password'],
            password2 = validated_data['password2'],
            subscribeCode = validated_data['subscribeCode'],
            grade = validated_data['grade'],
            classNumber = validated_data['classNumber'],
            number = validated_data['number'],
        )
        return student
    class Meta:
        model = Student
        fields = ['name', 'username', 'password', 'password2', 'subscribeCode', 'grade', 'classNumber', 'number']


class StudentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class EmployeeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empolyee
        fields = '__all__'





class LoginSerializer(serializers.Serializer):
    # 1.
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    last_login = serializers.CharField(max_length=255, read_only=True)
    
    # 2.
    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        
        # 3.
        if username is None:
            raise serializers.ValidationError(
                'An username is required to log in.'
            )
        
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        
        # 4.
        user = authenticate(username=username, password=password)
        
        # 5.
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found'
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        
        # 6.
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        
        # 7.
        return {
            'username': user.username,
            'username': user.username,
            'last_login': user.last_login
        }