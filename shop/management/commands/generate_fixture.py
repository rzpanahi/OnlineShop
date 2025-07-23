import json
import random
from decimal import Decimal
from faker import Faker
from django.core.management.base import BaseCommand

fake = Faker()


def get_decimal(min_val, max_val):
    return round(Decimal(str(random.uniform(min_val, max_val))), 2)


class Command(BaseCommand):
    help = 'Generate fixture.json for Product, Cart, Order, etc.'

    def handle(self, *args, **kwargs):
        data = []

        category_count = 10
        product_count = 40
        user_count = 10
        cart_count = 10
        order_count = 10
        items_per_cart = 6
        items_per_order = 6

        for i in range(1, category_count + 1):
            category = {
                "model": "shop.category",
                "pk": i,
                "fields": {
                    "title": fake.word(),
                    "created_at": fake.date_time_this_year().isoformat(),
                    "updated_at": fake.date_time_this_year().isoformat(),
                    "deleted": False,
                }
            }
            data.append(category)

        for i in range(1, user_count + 1):
            user = {
                "model": "accounts.user",
                "pk": i,
                "fields": {
                    "username": fake.user_name(),
                    "email": fake.email(),
                    "mobile": fake.basic_phone_number(),
                    "password": "pbkdf2_sha256$260000$fakepassword",
                    "created_at": fake.date_time_this_year().isoformat(),
                    "updated_at": fake.date_time_this_year().isoformat(),
                    "deleted": False,
            }
            }
            data.append(user)

        for i in range(1, product_count + 1):
            product = {
                "model": "shop.product",
                "pk": i,
                "fields": {
                    "title": fake.word().capitalize(),
                    "description": fake.sentence(),
                    "price": str(get_decimal(10, 1000)),
                    "quantity": random.randint(1, 50),
                    "image": None,
                    "available": True,
                    "category": random.randint(1, category_count),
                    "created_at": fake.date_time_this_year().isoformat(),
                    "updated_at": fake.date_time_this_year().isoformat(),
                    "deleted": False,
                }
            }
            data.append(product)

        cart_pk = 1
        cart_item_pk = 1
        for i in range(cart_count):
            user_id = random.randint(1, user_count)
            total_price = Decimal("0.00")
            cart_item_ids = []
            for _ in range(items_per_cart):
                product_id = random.randint(1, product_count)
                quantity = random.randint(1, 3)
                price = get_decimal(10, 300)
                total_price += price * quantity

                cart_item = {
                    "model": "shop.cartitem",
                    "pk": cart_item_pk,
                    "fields": {
                        "price": str(price),
                        "quantity": quantity,
                        "product": product_id,
                        "cart": cart_pk,
                        "created_at": fake.date_time_this_year().isoformat(),
                        "updated_at": fake.date_time_this_year().isoformat(),
                        "deleted": False,
                    }
                }
                data.append(cart_item)
                cart_item_ids.append(cart_item_pk)
                cart_item_pk += 1

            cart = {
                "model": "shop.cart",
                "pk": cart_pk,
                "fields": {
                    "total_price": str(total_price),
                    "user": user_id,
                    "created_at": fake.date_time_this_year().isoformat(),
                    "updated_at": fake.date_time_this_year().isoformat(),
                    "deleted": False,
                }
            }
            data.append(cart)
            cart_pk += 1

        order_pk = 1
        order_item_pk = 1
        payment_pk = 1
        for i in range(order_count):
            user_id = random.randint(1, user_count)
            total_price = Decimal("0.00")
            for _ in range(items_per_order):
                product_id = random.randint(1, product_count)
                quantity = random.randint(1, 4)
                price = get_decimal(15, 500)
                total_price += price * quantity

                order_item = {
                    "model": "shop.orderitem",
                    "pk": order_item_pk,
                    "fields": {
                        "price": str(price),
                        "quantity": quantity,
                        "successful": random.choice([True, False]),
                        "order": order_pk,
                        "product": product_id,
                        "created_at": fake.date_time_this_year().isoformat(),
                        "updated_at": fake.date_time_this_year().isoformat(),
                        "deleted": False,
                    }
                }
                data.append(order_item)
                order_item_pk += 1

            order = {
                "model": "shop.order",
                "pk": order_pk,
                "fields": {
                    "total_price": str(total_price),
                    "user": user_id,
                    "created_at": fake.date_time_this_year().isoformat(),
                    "updated_at": fake.date_time_this_year().isoformat(),
                    "deleted": False,
                }
            }
            data.append(order)

            # Payment for order
            payment = {
                "model": "shop.payment",
                "pk": payment_pk,
                "fields": {
                    "amount": str(total_price),
                    "user": user_id,
                    "order": order_pk,
                    "successful": True,
                    "created_at": fake.date_time_this_year().isoformat(),
                    "updated_at": fake.date_time_this_year().isoformat(),
                    "deleted": False,
                }
            }
            data.append(payment)

            order_pk += 1
            payment_pk += 1

        with open("fixture.json", "w") as f:
            json.dump(data, f, indent=4)

        self.stdout.write(self.style.SUCCESS("fixture.json created with all related data."))
