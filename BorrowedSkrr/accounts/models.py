from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
import random
import string

n=10	# 문자의 개수(문자열의 크기)
rand_str = ""	# 문자열

for i in range(n):
    rand_str += str(random.choice(string.ascii_letters + string.digits))

class UserManager(BaseUserManager):
    # employee 생성
    def create_empolyee(self, name, username, password=None, password2=None, school=None, certificate=None, classNumber=None, number=None, schoolCode=None):
        if not name:
            raise ValueError('must have user name')
        if not username:
            raise ValueError('must have user username')
        if not password2:
            raise ValueError('must have user password2')
        if not school:
            raise ValueError('must have user school')
        if not certificate:
            raise ValueError('must have user certificate')
        empolyee = self.model(
            name = name,
            username = username,
            password = password,
            password2 = password2,
            school = school,
            certificate = certificate,
            schoolCode = rand_str

        )
        empolyee.password = make_password(password)
        empolyee.save(using=self._db)
        return empolyee
    
    # student 생성
    def create_student(self, name, username, password=None, password2=None, subscribeCode=None, grade=None, classNumber=None, number=None):
        if not name:
            raise ValueError('must have user name')
        if not username:
            raise ValueError('must have user username')
        if not password2:
            raise ValueError('must have user password2')
        if not subscribeCode:
            raise ValueError('must have user subscribeCode')
        if not grade:
            raise ValueError('must have user grade')
        if not classNumber:
            raise ValueError('must have user classNumber')
        if not number:
            raise ValueError('must have user number')
        student = self.model(
            name = name,
            username = username,
            password = password,
            password2 = password2,
            subscribeCode = subscribeCode,
            grade = grade,
            classNumber = classNumber,
            number = number,
        )
        student.password = make_password(password)
        student.save(using=self._db)
        return student

    # # 관리자 user 생성
    # def create_superuser(self, email, nickname, name, password=None):
    #     user = self.create_user(
    #         email,
    #         password = password,
    #         nickname = nickname,
    #         name = name
    #     )
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user


# Create your models here.
class Empolyee(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50, null=True, blank=True)
    school = models.CharField(max_length=50, unique=True)
    certificate = models.ImageField(upload_to="")
    schoolCode = models.CharField(max_length=50, blank=True, null=True)
    
    # # User 모델의 필수 field
    # is_active = models.BooleanField(default=True)    
    # is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()
    
    def __str__(self):
        return self.school


class Student(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50, null=True, blank=True)
    subscribeCode = models.CharField(max_length=50)
    grade = models.PositiveIntegerField()
    classNumber = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    isAllowed = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.name

