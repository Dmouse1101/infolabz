from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class productdetails(models.Model):
    propname = models.CharField(max_length=20)
    proprice = models.FloatField()
    prodesc = models.TextField()
    proimage = models.ImageField(upload_to='photos')

    def product_image(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.proimage.url))

    def __str__(self):
        return self.propname
