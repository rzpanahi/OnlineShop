from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title"]
    search_fields = ["title"]

    def delete_queryset(self, request, queryset):
        for category in queryset:
            category.delete()


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "available", "category"]
    list_filter = ["category"]
    search_fields = ["title", "category"]

    def delete_queryset(self, request, queryset):
        for product in queryset:
            product.delete()


class CartAdmin(admin.ModelAdmin):
    list_display = ["total_price", "user"]
    list_filter = ["user"]
    search_fields = ["user"]

    def delete_queryset(self, request, queryset):
        for cart in queryset:
            cart.delete()


class CartItemAdmin(admin.ModelAdmin):
    list_display = ["price", "quantity", "product", "cart"]
    list_filter = ["product", "cart"]
    search_fields = ["product", "cart"]

    def delete_queryset(self, request, queryset):
        for cartItem in queryset:
            cartItem.delete()


class OrderAdmin(admin.ModelAdmin):
    list_display = ["total_price", "user"]
    list_filter = ["user"]
    search_fields = ["user"]

    def delete_queryset(self, request, queryset):
        for order in queryset:
            order.delete()


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["user", "price", "quantity", "successful", "order",]
    list_filter = ["user", "order"]
    search_fields = ["user", "order"]

    def delete_queryset(self, request, queryset):
        for orderItem in queryset:
            orderItem.delete()


class PaymentAdmin(admin.ModelAdmin):
    list_display = ["amount", "user", "order", "successful"]
    list_filter = ["user", "order"]
    search_fields = ["user", "order"]

    def delete_queryset(self, request, queryset):
        for payment in queryset:
            payment.delete()


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartItem, CartItemAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)
