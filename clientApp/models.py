from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from sellerApp.models import Product, DiscountCoupon


ORDERS_STATUS = (
    ('Ожидание', 'waiting'),
    ('Одобренно', 'approved'),
    ('Отказано', 'approved'),
    ('Принято', 'accepted'),
    ('Доставлено', 'delivered')
)


# Create your models here.

class Client(User):
    delivery_address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.username}'


class Cart(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    general_price = models.PositiveIntegerField(default=0)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.cart.client.username


class Order(models.Model):
    user = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    discount_coupon = models.OneToOneField(DiscountCoupon, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(null=True)

    phone_number = models.CharField(max_length=255)
    order_date = models.DateTimeField(default=timezone.now)
    delivery_address = models.CharField(max_length=255)
    total_price = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=15, default='Ожидание', choices=ORDERS_STATUS)

    courier = models.ForeignKey(User, related_name='order_as_courier', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.order_date} - {self.status}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(f'{self.user} - {self.order_date} - {self.status}')
        return super().save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.order} - {self.product} - {self.quantity} - {self.price}'

