from django.db import models

# Create your models here.
class station(models.Model):
    station_name = models.CharField(max_length=30)
    station_duration = models.IntegerField(default=3)
    station_price = models.FloatField(default=3.5)

    def __str__(self):
        return self.station_name