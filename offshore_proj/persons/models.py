from django.db import models

# Create your models here.
class Person(models.Model):
    First_name = models.CharField("First Name", max_length=240)
    Last_name = models.CharField("Last Name", max_length=240)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    income = models.IntegerField()