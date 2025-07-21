from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()


class ProductAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for product in queryset:
            product.delete()


class CartAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for cart in queryset:
            cart.delete()


class CartItemAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for cartItem in queryset:
            cartItem.delete()


class OrderAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for order in queryset:
            order.delete()


class OrderItemAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for orderItem in queryset:
            orderItem.delete()


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartItem, CartItemAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)
