from django.shortcuts import render, redirect
from .models import insertproductdata
# Create your views here.
def indexpage(request):
    fetchdata = insertproductdata.objects.all()
    context = {
        'data':fetchdata
    }
    return render(request,'showproduct.html',context)

def addproduct(request):
    return render(request,'addproduct.html')

def insertproduct(request):
    proname = request.POST.get('pname')
    proprice = request.POST.get('pprice')
    prodesc = request.POST.get('pdesc')
    proimage = request.FILES['pimage']
    insertdata = insertproductdata(pname=proname,pprice=proprice,pdesc=prodesc,pimage=proimage)
    insertdata.save()
    return redirect('/')

def singleproduct(request, pid):
    pro_data = insertproductdata.objects.get(id=pid)
    context = {
        'data':pro_data
    }
    return render(request,'singleproduct.html',context)