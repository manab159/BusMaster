from django.db import models


class Customer(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    balance=models.PositiveIntegerField()
