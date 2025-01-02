from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Cart)
# admin.site.register(models.CartItem)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Payment)



class CartItemAdmin(admin.ModelAdmin):
    def delete_queryset(self, request, queryset):
        for cartItem in queryset:
            cartItem.delete()

admin.site.register(models.CartItem, CartItemAdmin)