from django.contrib import admin
from .models import Empolyee, Student, User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username')

admin.site.register(User, UserAdmin)

class EmpolyeeAdmin(admin.ModelAdmin):
    list_display = ('school', 'certificate', 'schoolCode')

admin.site.register(Empolyee, EmpolyeeAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('subscribeCode', 'grade', 'isAllowed')
    list_filter = ['subscribeCode', 'isAllowed']

admin.site.register(Student, StudentAdmin)