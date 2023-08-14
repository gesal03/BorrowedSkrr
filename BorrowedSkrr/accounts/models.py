from django.db import models

# Create your models here.
class Empolyee(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    school = models.CharField(max_length=50, unique=True)
    certificate = models.ImageField(upload_to="")
    schoolCode = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.school


class Student(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    subscribeCode = models.CharField(max_length=50)
    grade = models.PositiveIntegerField()
    classNumber = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    isAllowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

