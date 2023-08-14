from django.contrib import admin
from .models import Empolyee, Student
# Register your models here.

class EmpolyeeAdmin(admin.ModelAdmin):
    list_display = ('school', 'name', 'certificate', 'schoolCode')

admin.site.register(Empolyee, EmpolyeeAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'subscribeCode', 'grade', 'isAllowed')
    list_filter = ['subscribeCode', 'isAllowed']

admin.site.register(Student, StudentAdmin)