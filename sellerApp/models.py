from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(f'{self.title}')
        return super().save()


class Brand(models.Model):
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} - {self.country}'


class Product(models.Model):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)

    year = models.PositiveIntegerField(null=True)
    product_image = models.FileField(upload_to='photo/', null=True)
    volume = models.FloatField()
    alcohol_percentage = models.FloatField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    rating = models.FloatField(default=0, null=True)
    count = models.IntegerField()
    discount = models.IntegerField(null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.category.title} - {self.brand.title} - {self.price}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(f'{self.title} - {self.category.title} - {self.brand.title}')
        return super().save()


class DiscountCoupon(models.Model):
    symbolism = models.CharField(max_length=255)
    discount_quantity = models.FloatField()

    def __str__(self):
        return self.discount_quantity
