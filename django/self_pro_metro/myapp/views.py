from django.shortcuts import render, redirect
from .models import * 
# Create your views here.
def showindex(request):
    showdata = station.objects.all()
    context = {'showdata':showdata}
    return render(request,"index.html",context)

def bookmetro(request):
    if request.method == "POST":
        s1 = request.POST.get('first')
        s2 = request.POST.get('second')
        # print(s1,s2)
        s1 = int(s1)
        s2 = int(s2)
        route = None
        if(s1<s2):
            if(s1 and s2 <=18):
                route = "East - West"
                print()
            elif(s1 and s2 >18):
                if(s1 and s2 <=32):
                    route = "North - South"
                    print()
                # else:
                #     route = "North - West"
                #     print()
            else:
                if(s1 <=18 and s2 == 33):
                    route = "East - West"
                elif(s1 >18 and s2 == 33):
                    route = "North - West"
                else:
                    route = "none"
                print()
            print()
        elif (s1 == s2):
            route = "You have chose same Station"
            print()
        else:
            print()
        
    return redirect(showindex)

# def show_stations(request):
#     return context