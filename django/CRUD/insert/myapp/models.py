from django.db import models

# Create your models here.
class contactus(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)