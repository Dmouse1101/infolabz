from django.shortcuts import render
from .models import *
# Create your views here.
def viewproduct(request):
    prodata = productdetails.objects.all()
    context = {
        'data':prodata
    }
    return render(request,'manageproduct.html',context)