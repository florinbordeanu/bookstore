
from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models


from store.models import Product


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    items = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order: {self.items}'

    def order_value(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.items.values())

























