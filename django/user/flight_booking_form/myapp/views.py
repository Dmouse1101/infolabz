from django.shortcuts import render
from .models import submit_data
# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def submited(request):
    u_name = request.POST.get('name')
    u_lname = request.POST.get('last name')
    u_mail = request.POST.get('email')
    u_phn = request.POST.get('phone number')
    u_trip_type = request.POST.get('trip-type')
    u_trip_class = request.POST.get('trip-class')
    u_s_country = request.POST.get('start-country')
    u_e_country = request.POST.get('end-country')
    u_s_date = request.POST.get('start-date')
    u_s_time = request.POST.get('start-time')
    u_e_date = request.POST.get('end-date')
    u_e_time = request.POST.get('end-time')
    u_air_type = request.POST.get('airport-type')
    u_lugg = request.POST.get('luggage')
    u_air_l_name = request.POST.get('air-line-name')
    u_air_l_number = request.POST.get('air-line-number')
    u_adults = request.POST.get('adults')
    u_child = request.POST.get('child')
    u_hotel_type = request.POST.get('hotel-type')
    u_vehicle = request.POST.get('vehicle')
    u_p_num = request.POST.get('passport-number')
    u_p_e_date = request.POST.get('passport_exp_date')
    u_msg = request.POST.get('Message')

    content = {
        'pName':u_name,
        'pLname':u_lname,
        'pMail':u_mail,
        'pPhn':u_phn,
        'pTrip':u_trip_type,
        'pTripClass':u_trip_class,
        'pStartCountry':u_s_country ,
        'pEndCountryp':u_e_country ,
        'pStartDate':u_s_date ,
        'pStartTime':u_s_time,
        'pEndDate':u_e_date ,
        'pEndTime':u_e_time,
        'pAirType':u_air_type,
        'pLugg':u_lugg ,
        'pAirName':u_air_l_name,
        'pAirNum':u_air_l_number,
        'pAdults':u_adults ,
        'pChild':u_child ,
        'pHotelType':u_hotel_type,
        'pVehicle':u_vehicle ,
        'pPassNum':u_p_num ,
        'pPassExpNum':u_p_e_date,
        'pMsg':u_msg
    }

    insertdata = submit_data(
        pName=u_name,
        pLname=u_lname,
        pMail=u_mail,
        pPhn=u_phn,
        pTrip=u_trip_type,
        pTripClass=u_trip_class,
        pStartCountry=u_s_country ,
        pEndCountryp=u_e_country ,
        pStartDate=u_s_date ,
        pStartTime=u_s_time,
        pEndDate=u_e_date ,
        pEndTime=u_e_time,
        pAirType=u_air_type,
        pLugg=u_lugg ,
        pAirName=u_air_l_name,
        pAirNum=u_air_l_number,
        pAdults=u_adults ,
        pChild=u_child ,
        pHotelType=u_hotel_type,
        pVehicle=u_vehicle ,
        pPassNum=u_p_num ,
        pPassExpNum=u_p_e_date,
        pMsg=u_msg
    )
    insertdata.save()
    return render(request,'submitdetail.html',content)