from django.db import models
from django.utils import timezone
from datetime import datetime



class Contact(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    unitNumber = models.IntegerField()
    civicNumber = models.IntegerField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=2)
    postalCode = models.CharField(max_length=3)
    createdAt = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.firstName + ' ' + self.lastName
    



