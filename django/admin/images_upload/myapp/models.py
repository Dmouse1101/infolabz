from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class book(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='photo')
    publish_date = models.DateTimeField(auto_now=True,editable=False)

    def admin_photo(self):
        return mark_safe("<img src='{}' width='100'".format(self.image.url))

    admin_photo.allow_tags = True
