from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Firm(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    OPTIONS = (
        ('i', 'In'),
        ('o', 'Out')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=1, choices=OPTIONS, default='i')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.IntegerField()
    price_total = models.IntegerField()

    def __str__(self):
        return f'{self.transaction_type} - {self.product}'

    


