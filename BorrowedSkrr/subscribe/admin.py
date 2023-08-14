from django.contrib import admin
from .models import EmpolyeeWishList, Shopping, Subscribe, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'likes', 'categroy')

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
    list_display = ('get_EmpolyeeSchool', 'get_productName', 'count', 'startDate', 'endDate')
    list_filter = ['empolyee_id', 'product_id']

    def get_EmpolyeeSchool(self, obj):
        return obj.empolyee_id.school
    
    def get_productName(self, obj):
        return obj.product_id.name

admin.site.register(Subscribe, SubscribeAdmin)