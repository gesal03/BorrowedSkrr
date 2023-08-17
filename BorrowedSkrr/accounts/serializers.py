from rest_framework import serializers
from .models import Empolyee, Student

class EmpolyeeSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        empolyee = Empolyee.objects.create_empolyee(
            name = validated_data['name'],
            username = validated_data['username'],
            password = validated_data['password'],
            password2 = validated_data['password2'],
            school = validated_data['school'],
            certificate = validated_data['certificate'],
            #schoolCode = validated_data['schoolCode']
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

