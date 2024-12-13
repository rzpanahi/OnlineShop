from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField()
    image = models.ImageField()
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Cart(models.Model):
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField()
    successful = models.BooleanField(default=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    successful = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
