from django.db import models
from accounts.models import User
from store.models import Product


class RentBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Product, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    address = models.CharField(max_length=255, blank=False)
    rent_date = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price_rent = models.DecimalField(max_digits=4, decimal_places=2, default=2.00)

    def rent_period(self):
        from_date = self.start_date
        to_date = self.end_date
        result = to_date - from_date
        return result.days

    def total_price(self):
        return self.price_rent*self.rent_period()







