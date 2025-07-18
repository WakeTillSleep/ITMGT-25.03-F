from django.db import models
from django.contrib.auth.models import User

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

# CartItem Model
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} of {self.product} (User: {self.user.username})'

# Transaction Model
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'Transaction by {self.user.username} on {self.created_at}'

# LineItem Model
class LineItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.name} (Transaction ID: {self.transaction.id})'