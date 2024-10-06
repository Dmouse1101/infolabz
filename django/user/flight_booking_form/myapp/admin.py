from django.contrib import admin
from .models import submit_data
# Register your models here.

class submit_server(admin.ModelAdmin):
    list_display = ['pName','pLname','pMail','pPhn','pTrip','pTripClass','pStartCountry','pEndCountryp','pStartDate','pStartTime','pEndDate','pEndTime','pAirType','pLugg','pAirName','pAirNum','pAdults','pChild','pHotelType','pVehicle','pPassNum','pPassExpNum','pMsg','timestamp']

admin.site.register(submit_data,submit_server)