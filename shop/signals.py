from django.db.models.signals import post_save
from django.dispatch import receiver

from models import Product, Order, Cart, CartItem, OrderItem


@receiver(post_save, sender=Product)
def soft_delete_product(sender, instance: Product, created, **kwargs):
    if not created:
        if instance.deleted:
            cart_item = CartItem.objects.filter(product=instance)
            for cartItem in cart_item:
                cartItem.delete()

            order_item = OrderItem.objects.filter(product=instance)
            for orderItem in order_item:
                orderItem.delete()


@receiver(post_save, sender=Order)
def soft_delete_order(sender, instance:Order, created, **kwargs):
    if not created:
        if instance.deleted:
            order_item = OrderItem.objects.filter(order=instance)
            for orderItem in order_item:
                orderItem.delete()

@receiver(post_save, sender=Cart)
def soft_delete_order(sender, instance:Cart, created, **kwargs):
    if not created:
        if instance.deleted:
            cart_item = CartItem.objects.filter(order=instance)
            for cartItem in cart_item:
                cartItem.delete()
