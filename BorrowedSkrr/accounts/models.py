from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, name, username, password=None):
        if not name:
            raise ValueError('must have user email')
        if not username:
            raise ValueError('must have user nickname')
        if not name:
            raise ValueError('must have user name')
        user = self.model(
            username = username,
            name = name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, name, username, password=None):
        user = self.create_user(
            username=username,
            password = password,
            name = name
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'username'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['name']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.name
    
class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    subscribeCode = models.CharField(max_length=50)
    grade = models.PositiveIntegerField()
    classNumber = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    isAllowed = models.BooleanField(default=False)

class Empolyee(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    school = models.CharField(max_length=50, unique=True)
    certificate = models.ImageField(upload_to="")
    schoolCode = models.CharField(max_length=50, blank=True, null=True)
