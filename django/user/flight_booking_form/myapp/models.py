from django.db import models
# Create your models here.

class submit_data(models.Model):
    pName = models.CharField(max_length=20)
    pLname = models.CharField(max_length=20)
    pMail = models.EmailField()
    pPhn = models.BigIntegerField()
    pTrip = models.CharField(max_length=20)
    pTripClass = models.CharField(max_length=20)
    pStartCountry = models.CharField(max_length=20)
    pEndCountryp = models.CharField(max_length=20)
    pStartDate = models.CharField(max_length=20)
    pStartTime = models.CharField(max_length=20)
    pEndDate = models.CharField(max_length=20)
    pEndTime = models.CharField(max_length=20)
    pAirType = models.CharField(max_length=20)
    pLugg = models.CharField(max_length=1)
    pAirName = models.CharField(max_length=20)
    pAirNum = models.CharField(max_length=20)
    pAdults = models.CharField(max_length=1)
    pChild = models.CharField(max_length=1)
    pHotelType = models.CharField(max_length=20)
    pVehicle = models.CharField(max_length=10)
    pPassNum = models.CharField(max_length=20)
    pPassExpNum = models.CharField(max_length=20)
    pMsg = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pName
