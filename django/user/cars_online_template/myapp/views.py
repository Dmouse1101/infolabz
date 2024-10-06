from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request,"index.html")

def aboutpage(request):
    return render(request,"about.html")

def contactpage(request):
    return render(request,"contact.html")

def newpage(request):
    return render(request,"new.html")

def singlepage(request):
    return render(request,"single.html")

def specialpage(request):
    return render(request,"specials.html")

def fourpage(request):
    return render(request,"404.html")