from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.TextField()
    quantity = models.BigIntegerField()
    productcategory = models.ForeignKey(category,verbose_name="Category",on_delete=models.CASCADE)