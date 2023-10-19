from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from django.conf import settings
# Create your models here.
class Customer(models.Model):
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        permissions = [
            ('view_history', 'Can view history')
        ]


class User(AbstractUser):
  email = models.EmailField(unique=True)





class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='orders')
    quantity = models.PositiveIntegerField()
    total_amount = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Calculate the total amount based on the product price and quantity
        self.total_amount = self.product.price * self.quantity

        if self.total_amount >= 50000:
            self.approved = False
        else:
            self.approved = True

        super().save(*args, **kwargs)

