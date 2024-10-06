from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class insertproductdata(models.Model):
    pname = models.CharField(max_length=20)
    pprice = models.FloatField()
    pdesc = models.TextField()
    pimage = models.ImageField(upload_to='photos')

    def product_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.pimage.url))

    def __str__(self):
        return self.pname
