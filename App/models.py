from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MessOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mess = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.mess 
    

class MessMenu(models.Model):
    user = models.OneToOneField(MessOwner, on_delete=models.CASCADE)
    item1 = models.CharField(max_length=50, blank=True)
    item2 = models.CharField(max_length=50, blank=True)
    item3 = models.CharField(max_length=50, blank=True)
    item4 = models.CharField(max_length=50, blank=True)
    item5 = models.CharField(max_length=50, blank=True)
    item6 = models.CharField(max_length=50, blank=True)
    item7 = models.CharField(max_length=50, blank=True)
    item8 = models.CharField(max_length=50, blank=True)
    item9 = models.CharField(max_length=50, blank=True)
    item10 = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.mess
    

class Customer(models.Model):
    mess = models.ForeignKey(MessOwner, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    registration = models.DateField()
    contact = models.CharField(max_length=15)
    type = models.CharField(max_length=10)
    per_month = models.IntegerField()

    def __str__(self):
        return self.full_name
    

class Attendance(models.Model):
    customer = models.ForeignKey(Customer,  on_delete=models.CASCADE)
    date = models.DateField()
    morning = models.BooleanField()
    evening = models.BooleanField()

    def __str__(self):
        return self.customer.full_name
    

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.email
    