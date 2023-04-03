from django.db import models

class ContactInformation(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()

# Create your models here.
