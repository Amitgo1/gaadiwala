from django.db import models

class ContactDetails(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    Phone = models.CharField(max_length=12)
    Message= models.TextField(max_length=150)
    # itna kaam karke ek query chalao python manage.py makemigration
    # fir ek query aur chalao python manage.py migrate
    
class NewsLetter(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
