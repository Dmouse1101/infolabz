from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request,"index.html")

def firstpage(request):
    return render(request,"first.html")
def secondpage(request):
    return render(request,"second.html")

def thirdpage(request):
    return render(request,"third.html")

def fourthpage(request):
    return render(request,"fourth.html")

def fifthpage(request):
    return render(request,"fifth.html")