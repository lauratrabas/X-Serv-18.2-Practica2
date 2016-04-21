from django.db import models

# Create your models here.

class Url (models.Model):
    original_url = models.TextField() 
