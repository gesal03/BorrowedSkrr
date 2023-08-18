from django.contrib import admin
from .models import EmpolyeeWishList, Shopping, Subscribe, Product, Management, Reservation, StudentWishList, StudentInfo, SubscribeInfo
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count', 'likes', 'category')

admin.site.register(Product, ProductAdmin)

class EmpolyeeWishListAdmin(admin.ModelAdmin):
    list_display = ('get_EmpolyeeSchool', 'get_productName')
    list_filter = ('empolyee_id', 'product_id')

    def get_EmpolyeeSchool(self, obj):
        return obj.empolyee_id.school
    
    def get_productName(self, obj):
        return obj.product_id.name
    
admin.site.register(EmpolyeeWishList, EmpolyeeWishListAdmin)

class ShoppingAdmin(admin.ModelAdmin):
    list_display = ('get_EmpolyeeSchool', 'get_productName', 'count', 'startDate', 'endDate')
    list_filter = ['empolyee_id', 'product_id']

    def get_EmpolyeeSchool(self, obj):
        return obj.empolyee_id.school
    
    def get_productName(self, obj):
        return obj.product_id.name

admin.site.register(Shopping, ShoppingAdmin)

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_EmpolyeeSchool', 'get_productName', 'count', 'startDate', 'endDate', 'isAllowed')
    list_filter = ['empolyee_id', 'product_id']

    def get_EmpolyeeSchool(self, obj):
        return obj.empolyee_id.school
    
    def get_productName(self, obj):
        return obj.product_id.name

admin.site.register(Subscribe, SubscribeAdmin)

class ManagementAdmin(admin.ModelAdmin):
    list_display = ('empolyee_id', 'student_id', 'requestDate')

    def get_EmpolyeeSchool(self, obj):
        return obj.empolyee_id.school
    
    def get_studentName(self, obj):
        return obj.student_id
    
admin.site.register(Management, ManagementAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('get_EmpolyeeSchool', 'get_studentName', 'get_productName', 'startDate')

    def get_EmpolyeeSchool(self, obj):
        return obj.empolyee_id.school
    
    def get_studentName(self, obj):
        return obj.student_id.name
    
    def get_productName(self, obj):
        return obj.subscribe_id.product_id.name
    
admin.site.register(Reservation, ReservationAdmin)

class StudentWishListAdmin(admin.ModelAdmin):
    list_display = ('get_studentName', 'get_productName')

    def get_studentName(self, obj):
        return obj.student_id.name
    
    def get_productName(self, obj):
        return obj.subscribe_id.product_id.name
    
admin.site.register(StudentWishList, StudentWishListAdmin)

class StudentInfoAdimn(admin.ModelAdmin):
    list_display =('name', 'belong', 'date', 'state')
admin.site.register(StudentInfo, StudentInfoAdimn)

class SubscribeInfoAdmin(admin.ModelAdmin):
    list_display=('name', 'count', 'start_date', 'end_date', 'price')
admin.site.register(SubscribeInfo, SubscribeInfoAdmin)