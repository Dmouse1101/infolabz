from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request,'home.html')

def bookspage(request):
    return render(request,'books.html')

def purchasepage(request):
    return render(request,'purchase.html')