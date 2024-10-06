from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
# Create your views here.

def checksession(request):
    try:
        uid = request.session['login_id']
        userdata = Login.objects.get(id=uid)

        vet = False
        if userdata.role == 'vet':
           vet = True
        try:
            profiledata = UserDetail.objects.get(id=uid)
        except UserDetail.DoesNotExist:
            profiledata = None

        context={
            'uid':uid,
            'userdata':userdata,
            'vet':vet,
            'profiledata':profiledata
        }
        return context
    except:
        pass
def indexpage(request):
    context = checksession(request)
    return render(request,'index.html',context)

def aboutpage(request):
    context = checksession(request)
    return render(request,'about.html',context)

def blogpage(request):
    context = checksession(request)
    return render(request,'blog.html',context)

def single_blogpage(request):
    context = checksession(request)
    return render(request,'blog-single.html',context)

def contactpage(request):
    context = checksession(request)
    return render(request,'contact.html',context)

def elementpage(request):
    context = checksession(request)
    return render(request,'elements.html',context)

def emailpage(request):
    context = checksession(request)
    return render(request,'email.html',context)

def errorpage(request):
    context = checksession(request)
    return render(request,'error.html',context)

def land_singlepage(request):
    context = checksession(request)
    return render(request,'landing-single.html',context)

def servicepage(request):
    context = checksession(request)
    return render(request,'services.html',context)

def loginpage(request):
    context = checksession(request)
    return render(request,'login.html',context)

def loginuser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pwd = request.POST.get('password')
    try:
        chkuser = Login.objects.get(email=email)
        if chkuser.password == pwd:
            request.session['login_id'] = chkuser.id
            messages.success(request,"Login Successfully")
            return redirect(indexpage)
        else:
            messages.error(request,"password not match")
            return render(request,'login.html')
    except Login.DoesNotExist:
        messages.error(request,"Incorrect Details !!!")
        return render(request,'login.html')
    return redirect(indexpage)

def logoutuser(request):
    del request.session['login_id']
    return redirect(indexpage)
def registerpage(request):
    context = checksession(request)
    return render(request,'register.html',context)

def registeruser(request):
    try:
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        role = request.POST.get('role')
        pwd = request.POST.get('password1')
        pwd1 = request.POST.get('password2')

        if Login.objects.filter(email=email).exists():
            messages.error(request,"Email already Exist")
            return redirect(registerpage)
        else:
            if pwd == pwd1:
                insertdata = Login(firstname=firstname,lastname=lastname, email=email,phone=phone, password= pwd,role=role)
                insertdata.save()
                messages.success(request,"Register Successfully")
                return redirect(loginpage)
    except:
        pass
    return render(request,'index.html')