import re
from .models import contactus
from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request,'index.html')

def fetchcontactus(request):
    uname = request.POST.get('uname')
    uemail = request.POST.get('uemail')
    uphone = request.POST.get('uphone')
    umessage = request.POST.get('umessage')

    insertdata = contactus(name=uname,email=uemail,phone=uphone,message=umessage)
    insertdata.save()
    return render(request,'index.html')
